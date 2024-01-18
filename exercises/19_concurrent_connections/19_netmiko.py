from datetime import datetime
import logging
import netmiko
import yaml
import os


# эта строка указывает, что лог-сообщения paramiko будут выводиться
# только если они уровня WARNING и выше
logging.getLogger("paramiko").setLevel(logging.WARNING)

logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)


def send_show(device, show):
    start_msg = '===> {} Connection: {}'
    received_msg = '<=== {} Received:   a{}'
    ip = device["host"]
    logging.info(start_msg.format(datetime.now().time(), ip))

    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(show)
        logging.info(received_msg.format(datetime.now().time(), ip))
    return result


if __name__ == "__main__":
    PASSWORD = os.environ.get('SSH_PASSWORD')
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
        devices[0]['password'] = PASSWORD
    for dev in devices:
        print(send_show(dev, 'ip a'))
