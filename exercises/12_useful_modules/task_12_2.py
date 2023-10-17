# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
import ipaddress
iplist = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
result = []
result2 = []
for ip in iplist:
    if "-" in ip:
        start_ip,end_ip=ip.split("-")
        start_ip=ipaddress.ip_address(start_ip)
        if len(end_ip.split('.'))!=4:
            end_ip=start_ip+int(end_ip)-1
        else:
            end_ip=ipaddress.ip_address(end_ip)
        result.extend(ip for ip in ipaddress.summarize_address_range(start_ip, end_ip))
        print(result)
    else:
        result.append(ipaddress.ip_address(ip))
        print(result)
print(result)
for i in result:
    if type(i) == ipaddress.IPv4Address:
        result2.append(str(i))
    else:
        for ip in list(i):
            result2.append(str(ip))
print(result2)


