# modules/menu.py
import inquirer
import os
from utils import hosts_manager, ssh_manager, presets, translation

ttr = translation.Locale('lang')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_user():
    print('\n')
    input("Press Enter to continue...")

def main_menu():
    while True:
        clear_screen()
        selected = inquirer.prompt([inquirer.List('language', message="Select a language", choices=ttr)])
        lenguage = selected['language']
        choices = [
            ttr.text(lenguage, "Add new login data"),
            ttr.text(lenguage, "List of hosts"),
            ttr.text(lenguage, "Interactive execute on all"),
            ttr.text(lenguage, "Presets"),
            ttr.text(lenguage, "Exit")
        ]
        question = [inquirer.List('choice', message="Select an option", choices=choices)]
        answer = inquirer.prompt(question)

        if answer['choice'] == choices[0]:
            hosts_manager.add_host()
        elif answer['choice'] == choices[1]:
            hosts_manager.list_hosts()
            wait_user()
        elif answer['choice'] == choices[2]:
            ssh_manager.execute_on_all()
            wait_user()
        elif answer['choice'] == choices[3]:
            presets.presets_menu()
            wait_user()
        elif answer['choice'] == choices[4]:
            break
