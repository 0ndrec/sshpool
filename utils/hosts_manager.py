# modules/hosts_manager.py
import json
import os
import inquirer
import re

HOSTS_FILE = 'hosts.json'


# Regex for validating host data
HOST_REGEX = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
USER_REGEX = re.compile(r'^[a-zA-Z0-9_]+$')
PASS_REGEX = re.compile(r'^[a-zA-Z0-9_]+$')
KEY_REGEX = re.compile(r'^[a-zA-Z0-9_]+$')

def load_hosts():
    if not os.path.exists(HOSTS_FILE):
        return []
    if os.path.getsize(HOSTS_FILE) == 0:
        return []
    with open(HOSTS_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print("Error: 'hosts.json' contains invalid JSON. Resetting hosts list.")
            return []

def save_hosts(hosts):
    with open(HOSTS_FILE, 'w') as f:
        json.dump(hosts, f, indent=4)

def add_host():
    questions = [
        inquirer.Text('host', message="Host/IP"),
        inquirer.Text('username', message="Username"),
        inquirer.Password('password', message="Password (leave blank if using key file)"),
        inquirer.Text('key_file', message="Key File Path (leave blank if using password)")
    ]
    answers = inquirer.prompt(questions)

    if not HOST_REGEX.match(answers['host']):
        print("Error: Invalid host format.")
        return
    if not USER_REGEX.match(answers['username']):
        print("Error: Invalid username format.")
        return
    
    hosts = load_hosts()
    hosts.append(answers)
    save_hosts(hosts)
    print("Host added successfully.")

def list_hosts():
    hosts = load_hosts()
    if not hosts:
        print("No hosts available.")
        return
    for idx, host in enumerate(hosts, 1):
        print(f"{idx}. {host['username']}@{host['host']}")


# storing format:
# [{"host": "192.168.1.178","username": "user","password": "toor","key_file": ""}, {"host": "192.168.1.177","username": "user","password": "toor","key_file": ""}]
