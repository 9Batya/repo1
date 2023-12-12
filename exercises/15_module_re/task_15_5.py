# -*- coding: utf-8 -*-
"""
Задание 15.5

Создать функцию generate_description_from_cdp, которая ожидает как аргумент
имя файла, в котором находится вывод команды show cdp neighbors.

Функция должна обрабатывать вывод команды show cdp neighbors и генерировать
на основании вывода команды описание для интерфейсов.

Например, если у R1 такой вывод команды:
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1

Для интерфейса Eth 0/0 надо сгенерировать такое описание
description Connected to SW1 port Eth 0/1

Функция должна возвращать словарь, в котором ключи - имена интерфейсов,
а значения - команда задающая описание интерфейса:
'Eth 0/0': 'description Connected to SW1 port Eth 0/1'


Проверить работу функции на файле sh_cdp_n_sw1.txt.
"""
import re
from pprint import pprint
def parse_cdp(filename1):
    regex = (r'\S+ +(\S+ \d/\d) +\d+ + R S I +\d+ +(\S+ \d/\d)')
    portown = []
    portcdp = []
    with open(filename1) as f:
        match_all = re.findall(regex, f.read())
        for port1, port2 in match_all:
            portown.append(port1)
            portcdp.append(f'description Connected to SW1 port {port2}')
    result = dict(zip(portown,portcdp))


    return result



pprint(parse_cdp('sh_cdp_n_sw1.txt'))
