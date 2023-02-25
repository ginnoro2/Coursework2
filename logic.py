import subprocess
import tkinter.messagebox as messagebox
import mysql.connector as mysql
from mysql.connector import Error


def Login(uname, pwd):
    conn = mysql.connect(host="localhost", user="root", password="", database="db_member")
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute(f"SELECT username, password FROM member WHERE username = '{uname}' AND password = '{pwd}'")
        
        result = cursor.fetchone()
        conn.close()
         

def Table():
    conn = mysql.connect(host="localhost", user="root", password="", database="db_member")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS member;")
    cursor.execute(
        "CREATE TABLE member(username varchar(255),password varchar(255),firstname varchar(255),lastname varchar(255))")
    conn.commit()
    conn.close()


def Register(username_val, password_val, firstname_val, lastname_val):
	Connect_db()
	conn = mysql.connect(host="localhost", user="root", password="", database="db_member")
	if conn.is_connected():
	    cursor = conn.cursor()
	    query = "INSERT INTO member(username, password, firstname, lastname) VALUES(%s, %s, %s, %s)"
	    cursor.execute(query, (username_val, password_val, firstname_val, lastname_val))
	    conn.commit()
	    
	    cursor.close()
	    conn.close()


def Connect_db():
	Database()
	conn = mysql.connect(host="localhost", user="root", password="", database="db_member")
	if conn.is_connected():
		cursor = conn.cursor()
		
		conn.close()

	
def Database():
	conn = mysql.connect(host="localhost", user="root", password="")
	if conn.is_connected():
		cursor = conn.cursor()
		# error handling while creating database
		try:
			cursor.execute(f"IF NOT EXISTS(SELECT * FROM sys.databases WHERE name = 'db_member')")
			cursor.execute(f"CREATE DATABASE db_member")
			
			conn.commit()
			print("database created")
			cursor.close()
			conn.close()
		
		except Error as e:
			pass
			conn.close()


def run_ping(target):
	output = subprocess.run(["Ping", "-c", "5", target], capture_output=True, text=True)
	return output.stdout



def run_nmap(target):
	output = subprocess.run(["Nmap", target], capture_output=True, text=True)
	return output.stdout



def run_searchsploit(target):
	output = subprocess.run(["Searchsploit", target], capture_output=True, text=True)
	return output.stdout



def run_netdiscover(target):
	output = subprocess.run(["netdiscover", target], capture_output=True, text=True)
	return output.stdout


if __name__ == "__main__":
	main()