# -*- coding: utf-8 -*-
"""
Задание 9.4

Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный
файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении
  у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются
с '!', а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.

Часть словаря, который должна возвращать функция (полный вывод можно посмотреть
в тесте test_task_9_4.py):
{
    "version 15.0": [],
    "service timestamps debug datetime msec": [],
    "service timestamps log datetime msec": [],
    "no service password-encryption": [],
    "hostname sw1": [],
    "interface FastEthernet0/0": [
        "switchport mode access",
        "switchport access vlan 10",
    ],
    "interface FastEthernet0/1": [
        "switchport trunk encapsulation dot1q",
        "switchport trunk allowed vlan 100,200",
        "switchport mode trunk",
    ],
    "interface FastEthernet0/2": [
        "switchport mode access",
        "switchport access vlan 20",
    ],
}

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "configuration"]


ignore = ["duplex", "alias", "Current configuration"]
ignore = ["duplex", "alias", "Current configuration"]
def ignore_command(command, ignore):
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status
def convert_config_to_dict (config_filename):
    result = {}
    with open(config_filename,'r') as f:
        interface = None
        for line in f:
            l1 = []
            if (line.split(' ')[0]).startswith('!') or (line.split(' ')[0]).startswith('\n'):
                interface = None
                continue
            if ignore_command(line,ignore) == True:
                pass
            elif 'interface' in line:
                interface = line.strip()
                result[interface] = []
            elif interface == None:
                result[line.strip()]=[]
            else:
                result[interface].append(line.strip())
    return result
a = convert_config_to_dict('config_sw1.txt')
print(a)
