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
for i in ip:
    if int(ip[0]) <= 224 and int(ip[1]) != 0:
        print('unicat')
        break
    if int(ip[0]) <= 239 and int(ip[1]) != 0:
        print('multicast')
        break
    if int(i) !=255:
        pass
    else:
        print ('broadcast')
        break
    if int(i) !=0:
        pass
    else:
        print('unassigned')
        break
    if 239 < int(ip[0]) < 255:
        print ('unassigned')
        break
