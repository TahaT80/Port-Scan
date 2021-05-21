"""
        API count exceeded - Increase Quota with Membership
        If you encounter an error (API count exceeded - Increase Quota with Membership)   you need a VPN

        creat by Amir Hossein Tadas & TAHA

        instagram = Taha_t_80
"""
import sys
import requests
from colorama import Fore
import os
def __start__():
    try:
        print(Fore.LIGHTBLACK_EX+"\n [!] Simple Port Scanner ! ! !")
        print(Fore.MAGENTA+"\n [!] Plase Enter IP/Domain\n")
        print(Fore.MAGENTA+"\n [!] for exampel : 158.58.188.67\n")
        inp = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"tahat80"+Fore.BLUE+"/"+Fore.WHITE+"Port-Scan"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+">> ")
        result = requests.get('https://api.hackertarget.com/nmap/?q=' + inp).text
        print(Fore.YELLOW+result)
        try:

            input(Fore.RED+" [!] "+Fore.GREEN+"Back To again (Press Enter...) ")
        except:
            print("")
            sys.exit()  
        
    except:
        print("\nExit :)")


if __name__ == '__main__':
    while True:
        try:
            os.system('cls')
        except:
            os.system('clear')

        __start__()
