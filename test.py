import os
import time
from colorama import init, Fore, Style
from sys import argv
from platform import uname, architecture
from getpass import getuser
from cpuinfo import get_cpu_info

import systemFiles.social_deanon as sd
import systemFiles.ip_deanon as idn
import systemFiles.phone_deanon as phd
import systemFiles.configs as conf
from systemFiles.debug import *

init()

red = Fore.RED
green = Fore.GREEN
reset = Style.RESET_ALL


def logo():
    logo_text = """\n\n
 ██████╗░███████╗░█████╗░███╗░░██╗░█████╗░███╗░░██╗
 ██╔══██╗██╔════╝██╔══██╗████╗░██║██╔══██╗████╗░██║
 ██║░░██║█████╗░░███████║██╔██╗██║██║░░██║██╔██╗██║
 ██║░░██║██╔══╝░░██╔══██║██║╚████║██║░░██║██║╚████║
 ██████╔╝███████╗██║░░██║██║░╚███║╚█████╔╝██║░╚███║
 ╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚══╝
    """

    os.system('cls' if os.name == 'nt' else 'clear')

    if conf.logo_animation == True:
        for line in logo_text.split('\n'):
            print(line)
            time.sleep(0.1)
    else:
        print(logo_text)

    print(Style.BRIGHT + ' Разработчик:       version: 0.0.2        ChasoniCK' + reset)
    time.sleep(conf.logo_time)


def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print(' Разработчик: ChasoniCK\n')
        print(' Вы в главном меню')
        print(' 1) Проверка по нику\n 2) Проверка IP-adress \n'
              ' 3) Проверка по номеру телефона\n 4) Проверка BSSID\n 5) Открыть debug меню')
        print(' 0) ! ВЫХОД ! \n')
        
        user_input = input(' $> ')

        if not user_input:
            continue


        try:
            home_page = int(user_input)
        except ValueError:
            print(red + ' Введите существующий пункт меню! (Только цифры)' + reset)
            time.sleep(0.5)
            continue

        if home_page == 0:
            break
        elif home_page == 1:
            sd.SocialDeanon()
        elif home_page == 2:
            idn.IpInfo()
        elif home_page == 3:
            phd.PhoneNumber()
        elif home_page == 4:
            idn.bssid_info()
        elif home_page == 5:
            debug_func()
        else:
            print(red + ' Введите существующий пункт меню!' + reset)
            time.sleep(0.7)


if __name__ == '__main__':
    if "-debug" in argv:
        debug_func()
    else:
        if conf.show_logo == True:
            logo()
        if conf.show_only_logo == False:
            menu()
