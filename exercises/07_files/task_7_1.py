# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
#!/usr/bin/env python3
with open ('ospf.txt','r') as f:
    for line in f:
        a=line.split()
        print ('''        Prefix {:17}
        AD/Metric {:17}
        Next-Hop {:17}
        Last update {:17}
        Outbound Interface {:17}'''.format(a[1],a[2],a[3],a[4],a[5]))
