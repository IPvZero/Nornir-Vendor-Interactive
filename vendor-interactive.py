from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir.plugins.functions.text import print_result
from nornir.core.filter import F
import os
import colorama
from colorama import Fore, Style

clear_command = "clear"
print("\n")
print(Fore.YELLOW + "#" * 70 + Style.RESET_ALL)
print(" " * 20 + "Welcome to " + Fore.RED + "Nornir!" + Style.RESET_ALL)
print(" " * 15 + "This is a Dynamic script!")
print(Fore.YELLOW + "#" * 70 + Style.RESET_ALL)
targets = input ("\n" + Fore.CYAN + "Please enter the vendor you wish to target: " + Style.RESET_ALL)
os.system(clear_command)
print(Fore.YELLOW + "#" * 70 + Style.RESET_ALL)
print("\n You have selected " + Style.BRIGHT + Fore.MAGENTA + targets + Style.RESET_ALL)
print("\n Please enter the commands you wish to execute, separated by commas")
print("Example: " + Fore.GREEN + "< show ip int brief, show ip route, show version >")
print(Fore.YELLOW + "#" * 70 + Style.RESET_ALL)
commands = input ("\nEnter Commands: ")
cmds = commands.split(",")
os.system(clear_command)
for cmd in cmds:
    nr = InitNornir()
    filtered = nr.filter(F(vendor=targets))

    result = filtered.run(
            task=send_command,name=Fore.RED + Style.BRIGHT + "COMMAND EXECUTED: " + Fore.GREEN + cmd.upper(),
        command=cmd
        )

    print_result(result)
