# modules/menu.py
import inquirer
import os
from utils import hosts_manager, ssh_manager, presets

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_user():
    print('\n')
    input("Press enter to continue...")

def main_menu():
    while True:
        clear_screen()
        choices = [
            "Add new login data",
            "List of hosts",
            "Interactive execute on all",
            "Presets",
            "Exit"
        ]
        question = [inquirer.List('choice', message="Select an option", choices=choices)]
        answer = inquirer.prompt(question)

        if answer['choice'] == "Add new login data":
            hosts_manager.add_host()
        elif answer['choice'] == "List of hosts":
            hosts_manager.list_hosts()
            wait_user()
        elif answer['choice'] == "Interactive execute on all":
            ssh_manager.execute_on_all()
            wait_user()
        elif answer['choice'] == "Presets":
            presets.presets_menu()
            wait_user()
        elif answer['choice'] == "Exit":
            break
