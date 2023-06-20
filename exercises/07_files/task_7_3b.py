# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
enter = input('Введите номер vlan: ')
result = {}
with open('CAM_table.txt') as f:
    for line in f:
        if 'Gi' in line:
            interface = line.split()[3]
            mac = line.split()[1]
            vlan = int(line.split()[0])
            result[vlan] = [interface, mac]
a = sorted(result)
put = enter.split(',')
for i in a:
    if any(int(g) == i for g in put):
        print("{:<5} {:>10} {:>20}".format(i, result[i][0], result[i][1]))
    else:
        pass
