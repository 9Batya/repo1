# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""
import re
from pprint import pprint


def parse_cdp(filename):
    regex = (r'interface (?P<int>\S+)'
             r'|ip address (?P<ip1>[\d.]+) (?P<ip2>[\d.]+)')

    result = {}

    with open(filename) as f:
        match_iter = re.finditer(regex, f.read())
        for match in match_iter:
            if match.lastgroup == 'int':
                device = match.group(match.lastgroup)
                result[device] = {}
            elif device:
                result[device] = match.group(2,3)

    list = []
    for key in result:
        if result[key] == {}:
            list.append(key)
    for key in list:
        del result[key]

    return result
pprint(parse_cdp('config_r1.txt'))
