# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции ping_ip_addresses:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""
import subprocess
from datetime import datetime
import logging
from concurrent.futures import ThreadPoolExecutor

logging.getLogger('subprocess').setLevel(logging.WARNING)

logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO,
)
def send_ping_to_hosts(ip_list,limit):
    ip_available = []
    ip_unreachable = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = executor.map(ping_check, ip_list)
        for ip, output in zip(ip_list, result):
            if output == True:
                ip_available.append(ip)
            if output == False:
                ip_unreachable.append(ip)
        return ip_available, ip_unreachable


def ping_check(ip_address):
    #шаблон для логера
    start_msg = '===> {} Проверяем доступность устройства {}'
    received_msg_sucsess = '<=== {} Устройство {} доступно'
    received_msg_unsucsess = '<=== {} Устройство {} недоступно'
    #пинг до устройства и запись результата в stdout
    result = subprocess.run(['ping', '-c', '3', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            encoding='utf-8')
    #Вывод результата, функция возвращает булево значение
    logging.info(start_msg.format(datetime.now().time(), ip_address))
    if result.returncode == 0:
        logging.info(received_msg_sucsess.format(datetime.now().time(), ip_address))
        return True
    else:
        logging.info(received_msg_unsucsess.format(datetime.now().time(), ip_address))
        return False

if __name__ == '__main__':
    print(send_ping_to_hosts(['8.8.8.8','192.168.1.118','vk.com'],3))
