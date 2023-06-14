# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input('Введите ип: ')
ip = ip.split('.')
while True:
    if any( i.isdigit() == False for i in ip ):
        print( 'Неправильный IP-адрес' )
    elif len(ip)!=4:
        print('Неправильный IP-адрес')
    elif any(int(i)>255 or int(i)<0 for i in ip):
        print ('Неправильный IP-адрес')
    else:
        break
    ip = input('Введите ип: ')
    ip = ip.split( '.' )
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
