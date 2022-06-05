#import
import time
import sys
import os
import requests
import colorama
#from
from time import sleep
from discord_webhook import DiscordWebhook
from colorama import Fore, init

os.system('cls' if os.name == 'nt' else 'clear')
banner = (Fore.LIGHTBLUE_EX + f"""
                                   ██   ██ ████████ ██ ███████ ██ ███████ 
                                   ██  ██     ██    ██ ██      ██ ██      
                                   █████      ██    ██ ███████ ██ ███████ 
                                   ██  ██     ██    ██      ██ ██      ██ 
                                   ██   ██    ██    ██ ███████ ██ ███████

                                              {Fore.LIGHTRED_EX}discord.gg/vecna
                                              {Fore.LIGHTRED_EX}github.com/deusweb                                        
""")
print(banner)
print(f'{Fore.YELLOW}|           {Fore.RESET}[{Fore.LIGHTBLUE_EX}1{Fore.RESET}] {Fore.LIGHTYELLOW_EX}Webhook Spammer{Fore.RESET} [{Fore.LIGHTBLUE_EX}2{Fore.RESET}] {Fore.LIGHTYELLOW_EX}Webhook Deleter{Fore.YELLOW} {Fore.RESET}[{Fore.LIGHTBLUE_EX}3{Fore.RESET}] {Fore.LIGHTYELLOW_EX}Webhook Change Name{Fore.YELLOW} {Fore.RESET}[{Fore.LIGHTBLUE_EX}4{Fore.RESET}] {Fore.LIGHTYELLOW_EX}Webhook Change Channel           |\n')
print(f'{Fore.LIGHTRED_EX}[>] {Fore.RESET}', end='')
choice = int(input(''))

if choice not in [1, 2, 3, 4]:
    print(f'\n{Fore.LIGHTYELLOW_EX}--------------------------------------------------------\n{Fore.MAGENTA}Option{Fore.RESET} = {Fore.RED}Error{Fore.RESET} : Invalid Choice!')
    time.sleep(1)
    print(f"{Fore.RED}Exiting...")
    time.sleep(3)

if choice == 1:
    print(f"{Fore.RED}Press CTRL+C to Exit when finished with the Spammer!")
    sleep(1.3)
    print(f"\n{Fore.LIGHTYELLOW_EX}--------------------------------------------------------\n{Fore.RESET}[{Fore.MAGENTA}1{Fore.RESET}]{Fore.LIGHTMAGENTA_EX} Webhook URL:{Fore.RESET}")
    webhook = str(input(f"{Fore.LIGHTRED_EX}\n[>]{Fore.RESET} "))
    print(f"\n{Fore.LIGHTYELLOW_EX}--------------------------------------------------------\n{Fore.RESET}[{Fore.MAGENTA}1{Fore.RESET}]{Fore.LIGHTMAGENTA_EX} Message:{Fore.RESET}")
    message = str(input(f"{Fore.LIGHTRED_EX}\n[>]{Fore.RESET} "))
    while True:
        _data = requests.post(webhook, json={'content': message}, headers={'Content-Type': 'application/json'})
        if _data.status_code == 204:
            print(f'[{Fore.LIGHTRED_EX}WEBHOOK SPAMMER LOG{Fore.RESET}] Sent a new message!')

if choice == 2:
  print(f"\n{Fore.LIGHTYELLOW_EX}--------------------------------------------------------\n{Fore.RESET}[{Fore.MAGENTA}1{Fore.RESET}]{Fore.LIGHTMAGENTA_EX} Webhook URL:{Fore.RESET}")
  webhook = str(input(f"{Fore.LIGHTRED_EX}\n[>]{Fore.RESET} "))
  requests.delete(webhook)
  print(f"{Fore.LIGHTGREEN_EX}Done! {Fore.RED}\nExiting now...")
  sleep(1)
  exit()

if choice == 3:
    print(f"\n{Fore.LIGHTYELLOW_EX}--------------------------------------------------------\n{Fore.RESET}[{Fore.MAGENTA}1{Fore.RESET}]{Fore.LIGHTMAGENTA_EX} Webhook URL:{Fore.RESET}")
    webhook = str(input(f"{Fore.LIGHTRED_EX}\n[>]{Fore.RESET} "))
    print(f"\n{Fore.LIGHTYELLOW_EX}--------------------------------------------------------\n{Fore.RESET}[{Fore.MAGENTA}1{Fore.RESET}]{Fore.LIGHTMAGENTA_EX} New Name Webhook:{Fore.RESET}")
    nwname = str(input(f"{Fore.LIGHTRED_EX}\n[>]{Fore.RESET} "))
    r = requests.patch(webhook, json={ "name":nwname })
    print(f"{Fore.LIGHTGREEN_EX}Succes change name! {Fore.RED}\nExiting now...")
    sleep(1)
    exit()

if choice == 4:
    print(f"\n{Fore.LIGHTYELLOW_EX}--------------------------------------------------------\n{Fore.RESET}[{Fore.MAGENTA}1{Fore.RESET}]{Fore.LIGHTMAGENTA_EX} Webhook URL:{Fore.RESET}")
    webhook = str(input(f"{Fore.LIGHTRED_EX}\n[>]{Fore.RESET} "))
    print(f"\n{Fore.LIGHTYELLOW_EX}--------------------------------------------------------\n{Fore.RESET}[{Fore.MAGENTA}1{Fore.RESET}]{Fore.LIGHTMAGENTA_EX} New Channel Id:{Fore.RESET}")
    channid = str(input(f"{Fore.LIGHTRED_EX}\n[>]{Fore.RESET} "))
    r = requests.patch(webhook, json={ "channel_id":channid })
    print(f"{Fore.LIGHTGREEN_EX}Succes change channel! {Fore.RED}\nExiting now...")
    sleep(1)
    exit()