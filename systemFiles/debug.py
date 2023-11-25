from colorama import init, Fore, Style
from sys import argv
from platform import uname, architecture
from getpass import getuser
from cpuinfo import get_cpu_info
from time import sleep
import systemFiles.configs as cfg

red = Fore.RED
green = Fore.GREEN
reset = Style.RESET_ALL

def debug_func():
    config_file = "systemFiles/configs.py"

    print(red + ' Не трогайте параметры, если не знаете, за что они отвечают' + reset)
    print(' Открыть лист команд - help')

    try:
        with open(config_file, 'r') as file:
            config_data = file.readlines()

        while True:
            user_input = input('\n $> ').strip().lower()

            if user_input == "show_config":
                print(green + f"[$] {getuser()}" + reset)
                for i, line in enumerate(config_data):
                    prefix = "╰" if i == len(config_data) - 1 else "├"
                    print(f" {prefix} {line.strip()}")

            elif user_input == "sys_info":
                system_info = uname()
                processor_info = get_cpu_info()['brand_raw']
                print(green + f"[$] {getuser()}" + reset)
                print(f" ├ Система: {system_info.system}, {architecture()[0]}")
                print(f" ├ Имя устройства: {system_info.node}")
                print(f" ├ Архитектура: {system_info.machine}")
                print(f" ╰ Процессор: {processor_info}")

            elif user_input == "version" or "v":
                print(green + f"[$] {getuser()}" + reset)
                print(f" ╰ Версия: {cfg.version}")

            elif user_input == "help":
                print(green + f"[$] {getuser()}" + reset)
                print( ' ├ show_config - Отображение всех конфигураций\n'
                       ' ├ sys_info - Открыть параметры устройства\n'
                       ' ╰ exit - Завершение')
                
            elif user_input == "exit":
                break

            else:
                parts = user_input.split('=')
                if len(parts) == 2:
                    variable_name = parts[0].strip()
                    variable_value = parts[1].strip()

                    if variable_value.lower() == "true":
                        variable_value = True
                    elif variable_value.lower() == "false":
                        variable_value = False

                    for i, line in enumerate(config_data):
                        if variable_name in line:
                            config_data[i] = f"{variable_name} = {variable_value}\n"
                            with open(config_file, 'w') as file:
                                file.writelines(config_data)
                            print(f' Значение "{variable_name}" обновлено в файле "{config_file}"')
                            break
                else:
                    print(red + ' Неверный формат ввода. Используйте: переменная = значение' + reset)
                    sleep(0.7)

    except FileNotFoundError:
        print(f' Файл "{config_file}" не найден.')
    except Exception as e:
        print(f" Произошла ошибка: {e}")