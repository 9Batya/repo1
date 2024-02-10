import sqlite3
import os
def check_file_db(db_filename):
    db_exists = os.path.exists(db_filename)
    return db_exists

def create_db(db_filename):
    conn = sqlite3.connect(db_filename)
    with open(schema_filename, 'r') as f:
        schema = f.read()
    conn.executescript(schema)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    schema_filename = 'dhcp_snooping_schema.sql'
    db_filename = 'dhcp_snooping.db'
    if check_file_db(db_filename):
        print('База данных существует')
    else:
        print('Создаю базу данных...')
        create_db(db_filename)