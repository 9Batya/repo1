# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input ('Введите ип: ')
ip = ip.split('.')
if int(ip[0]) <= 224 and int(ip[1]) != 0:
    print('unicast')
elif int(ip[0]) <= 239 and int(ip[1]) != 0:
    print('multicast')
elif all(int(i) == 255 for i in ip):
    print('local broadcast')
elif all(int(i) == 0 for i in ip):
    print('unassigned')
else:
    print('unused')
