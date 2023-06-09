# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

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
