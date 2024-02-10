import sqlite3
import yaml
import re

def insert_switches(yaml_file):
    #Создаем список котреджей из yaml файла switches.yml
    with open(yaml_file, 'r') as f:
        switches = yaml.safe_load(f)
    result = list(switches['switches'].items())

    return result

def insert_dhcp(text_file):
    #Создаем объект re для фильтрации строк
    regex = re.compile(r'(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')

    result = []
    #Открываем файл text_file и фильтруем строки
    for file in text_file:
        sw_name = file.split('_')[0]
        filtered = []
        with open(file) as data:
            for line in data:
                match = regex.search(line)
                if match:
                    filtered.append(match.groups())
        dict_filtered = {sw_name : filtered}
        result.append(dict_filtered)

    return result

def insert_switch_to_db(db_filename, table_switch):
    conn = sqlite3.connect(db_filename)

    for row in table_switch:
        try:
            with conn:
                query = '''insert into switches (hostname, location)
                           values (?, ?)'''
                conn.execute(query, row)
        except sqlite3.IntegrityError as e:
            print('Error occured: ', e)

    conn.close()
def insert_dhcp_to_db(db_filename, table_dhcp):

    conn = sqlite3.connect(db_filename)
    #ошибка в коде text not null references switches(hostname)
    for device in table_dhcp:
        for key, value in device.items():
            for row in value:
                try:
                    with conn:
                        query = f'''insert into dhcp (mac, ip, vlan, interface, switch)
                               values (?, ?, ?, ?,'{key}')'''
                        print(query)
                        conn.execute(query, row)
                except sqlite3.IntegrityError as e:
                    print('Error occured: ', e)

    conn.close()



if __name__ == '__main__':
    yaml_file = 'switches.yml'
    text_files = ['sw1_dhcp_snooping.txt','sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt']
    db_filename = 'dhcp_snooping.db'
    tuple_yaml = insert_switches(yaml_file)
    tuple_dhcp = insert_dhcp(text_files)
    print(tuple_dhcp)
    print(tuple_yaml)
    insert_switch_to_db(db_filename, tuple_yaml)
    insert_dhcp_to_db(db_filename, tuple_dhcp)


