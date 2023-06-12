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
if int(ip[1])<=224 and int(ip[1]) != 0:
    print ('unicat')
elif int(ip[1]) <= 239 and int(ip[1]) != 0:
    print ('multicast')
else:
    for i in ip:
        if int(i) !=255:
            break
        else:
            print ('broadcast')
        if int(i) !=0:
            break
        else:
            print ('unassigned')
        break
    else:
        print ('unused')
