# modules/presets.py
import inquirer
from utils.ssh_manager import ssh_command
from utils.hosts_manager import load_hosts
from multiprocessing import Pool

PRESETS = {
    "Check Disk Usage": "df -h",
    "List Running Processes": "ps aux",
    "Show Uptime": "uptime"
}

def presets_menu():
    choices = list(PRESETS.keys()) + ["Back"]
    question = [inquirer.List('preset', message="Select a preset command", choices=choices)]
    answer = inquirer.prompt(question)
    if answer['preset'] == "Back":
        return
    command = PRESETS[answer['preset']]
    hosts = load_hosts()
    if not hosts:
        print("No hosts available.")
        return
    with Pool(len(hosts)) as pool:
        pool.starmap(ssh_command, [(host, command) for host in hosts])
