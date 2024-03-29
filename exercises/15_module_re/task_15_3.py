# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""
import re
from pprint import pprint
def parse_cdp(filename1, filename2):
 regex = (r'ip nat inside source static tcp (?P<ip>[\d.]+) +'
          r'?P<sport>\d+) +'
          r'interface GigabitEthernet0/1 (?P<dport>\d+)')
 result = {}
 config = []
 with open(filename1) as f:
  match_iter = re.finditer(regex, f.read())
  for match in match_iter:
   config.append(match.groupdict())
   result['config'] = config
 with open(filename2, 'w') as f:
  for i in result['config']:
   f.write(f'''object network LOCAL_{i['ip']}
host 10.1.2.84
nat (inside,outside) static int service tcp {i['sport']} {i['dport']}\n''')
   return
