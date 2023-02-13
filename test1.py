#---------------Import Libraries---------------------------

from tkinter import *
import tkinter as tk
from tkinter import ttk
import subprocess
from tkinter import filedialog
import tkinter.messagebox
from tkinter import messagebox
import os
import mysql.connector as mysql
from mysql.connector import Error


#-------------Main window class----------------------------------------------------------------------------------------------------------------
class Window:
    def __init__(self, master):

        #Frame  
        self.mainFrame = Frame(master)
        self.mainFrame.pack(side=TOP,padx=100,  pady=100)
        
        #Button
        btn_login = Button(self.mainFrame, text="Begin",command = self.begin, font=('arial', 18), width=35 )
        btn_login.grid(row=4, columnspan=2, pady=20)

    #To close window    
    def begin(self):
        self.mainFrame.destroy()
        openwindow = Main()


#-------------Login window class---------------------------------------------------------------------------------------------------------------
class Main:     
    def __init__(self):
        #Main Login Frame
        Top = Toplevel()
    
        self.LoginFrame = Frame(Top)
        self.LoginFrame.pack(side=TOP,padx=100,  pady=100)
        
        #Label Username Password and result display
        lbl_username = Label(self.LoginFrame, text="Username:", font=('arial', 25), bd=18)
        lbl_username.grid(row=1)
        lbl_password = Label(self.LoginFrame, text="Password:", font=('arial', 25), bd=18)
        lbl_password.grid(row=2)
        self.lbl_result1 = Label(self.LoginFrame, text="", font=('arial', 18))
        self.lbl_result1.grid(row=3, columnspan=2)
        
        #Entry frame
        self.username = Entry(self.LoginFrame, font=('arial', 20), width=15)
        self.username.grid(row=1, column=1)
        self.password = Entry(self.LoginFrame, font=('arial', 20), width=15, show="*")
        self.password.grid(row=2, column=1)
        
        #Login Button
        btn_login = Button(self.LoginFrame, text="Login",command = self.Login, font=('arial', 18), width=35 )
        btn_login.grid(row=4, columnspan=2, pady=20)
       
        #Registry toggle button
        lbl_register = Label(self.LoginFrame, text="Register", fg="Blue", font=('arial', 12))
        lbl_register.grid(row=0, sticky=W)
        lbl_register.bind('<Button-1>', self.ToggleToRegister)
    
   
    def ToggleToRegister(self, event=None):
        self.LoginFrame.destroy()
        openwindow = Register()

    #login function definition   
    def Login(self):
        Database()
        #Error handling while connecting to the database
        try:
            conn = mysql.connect(host="localhost", user="root", password="", database="db_member")
            if conn.is_connected():
                cursor = conn.cursor()

        except Error as e:
            messagebox.showinfo("Host  not found")

        #Checking input field if it empty with prompt messabe
        if self.username.get() == "" and self.password.get() == "":
            self.lbl_result1.config(text="Please complete the required field!", fg="orange")
        
        #Storing user inputs in variable and matching values with table member from  database db_member.
        else:
            username = self.username.get()
            password = self.password.get()
            
            cursor.execute(f"SELECT username, password FROM member WHERE username = '{username}' AND password = '{password}'")
            result = cursor.fetchone()
                    
            if result is None:

                messagebox.showinfo("Invalid {username} or {password}")
                print("invalid")

            else:
                self.lbl_result1.config(text="You are successfully Logged Ind", fg="red")
                self.LoginFrame.destroy()
                openwindow = Netrecon()


#-------------Register window class------------------------------------------------------------------------------------------------------------
class Register:
    def __init__(self):
        #Frame
        top = Toplevel()
    
        self.RegisterFrame = Frame(top)
        self.RegisterFrame.pack(side=TOP, padx=100 ,pady=100)
        
        #Label
        lbl_username = Label(self.RegisterFrame, text="Username:", font=('arial', 18), bd=18)
        lbl_username.grid(row=1)
        lbl_password = Label(self.RegisterFrame, text="Password:", font=('arial', 18), bd=18)
        lbl_password.grid(row=2)
        lbl_firstname = Label(self.RegisterFrame, text="Firstname:", font=('arial', 18), bd=18)
        lbl_firstname.grid(row=3)
        lbl_lastname = Label(self.RegisterFrame, text="Lastname:", font=('arial', 18), bd=18)
        lbl_lastname.grid(row=4)
        self.lbl_result2 = Label(self.RegisterFrame, text="", font=('arial', 18))
        self.lbl_result2.grid(row=5, columnspan=2) 
        
        #Entry
        self.username = Entry(self.RegisterFrame, font=('arial', 20), width=15)
        self.username.grid(row=1, column=1)
        self.password = Entry(self.RegisterFrame, font=('arial', 20),  width=15, show="*")
        self.password.grid(row=2, column=1)
        self.firstname = Entry(self.RegisterFrame, font=('arial', 20), width=15)
        self.firstname.grid(row=3, column=1)
        self.lastname = Entry(self.RegisterFrame, font=('arial', 20),  width=15) 
        self.lastname.grid(row=4, column=1)
        
        #Button
        btn_Register = Button(self.RegisterFrame, text="Register", font=('arial', 18), width=35, command=self.register)
        btn_Register.grid(row=6, columnspan=2, pady=20)
        
        #Toggle Button
        lbl_login = Label(self.RegisterFrame, text="Login", fg="Blue", font=('arial', 12))
        lbl_login.grid(row=0, sticky=W)
        lbl_login.bind('<Button-1>',self.ToggleToLogin)

       
    def ToggleToLogin(self, event=None):
        self.RegisterFrame.destroy()
        Main()
       
    #Creating table
    def Table(self):
        Connect_db()
       
        cursor.execute("DROP TABLE IF EXISTS member;")

        cursor.execute("CREATE TABLE member(username varchar(255),password varchar(255),firstname varchar(255),lastname varchar(255))")
        
        conn.commit()
        messagebox.showinfo("Table exists")

        self.Exit()

    def Exit(self):
        root.destroy()
        exit()
    #Inserting into database
    def register(self):
        #Database()
        Connect_db()
        #getting user data
        USERNAME = self.username.get()
        PASSWORD = self.password.get()
        FIRSTNAME = self.firstname.get()
        LASTNAME = self.lastname.get()
        print(self.username.get())
        #connecting to the database
        conn = mysql.connect(host="localhost",user="root",password="",database="db_member")

        if conn.is_connected():
            #executing MySQL query to insert values to the talbe 
            cursor = conn.cursor()      
            query = "INSERT INTO member(username, password, firstname, lastname) VALUES(%s, %s, %s, %s)"
            cursor.execute(query,(USERNAME, PASSWORD, FIRSTNAME, LASTNAME))

            conn.commit()
            messagebox.showinfo("Registration Succesfull")
            self.lbl_result2.config(text="Successfully Created!", fg="black")
            cursor.close()
            conn.close()


#-------------Database connection class--------------------------------------------------------------------------------------------------------
class Connect_db:
    def __init_(self):
        Database()
        try:
            conn = mysql.connect(host="localhost",user="root",password="",database="db_member")
            if conn.is_connected():
                cursor = conn.cursor()

                conn.close()

        except Error as e:
            
            root.destroy() 

#-------------Create Database class----------------------------------------------------------------------------------------------------
class Database:
    def __init__(self):
        conn = mysql.connect(host="localhost",user="root",password="")
        if conn.is_connected():
            cursor =conn.cursor()
            #error handling while creating database
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
           
#-------------Main Reconnaissance window class------------------------------------------------------------------------------------------------ 
class Netrecon:
    def __init__(self):
        #Frame
        top = Toplevel()
        
        top_frame = Frame(top)
        top_frame.pack(side="top", fill="x")
        
        #Menubar
        menubar = Menu(top)
        file = Menu(menubar, tearoff=0)
        
        #Frame for buttons
        bottom_frame = Frame(top)
        bottom_frame.pack(side="bottom", fill="x")

        #Display terminal Frame
        main = Frame(top)
        main.pack(fill='both', expand=True)
        self.terminal = Text(main, wrap='word')
        self.terminal.pack(fill='both', expand=True)
        self.terminal1 = Text(main,height=10, width=30, wrap='word')
        self.terminal1.pack(fill='both', expand=True)
        
        #Entry 
        self.entry = Entry(top)
        self.entry.pack(side='top', fill='x')
        
        #Function Buttons
        nmap_button = Button(top_frame, text="Network Scan",command=self.run_nmap)
        nmap_button.pack(side='left')
        searchsploit_button = Button(top_frame, text="Exploit_db",command=self.run_searchsploit)
        searchsploit_button.pack(side='right')
        discover_button = Button(top_frame, text="Discover",command=self.run_netdiscover)
        discover_button.pack(side='left') 
        dns_button = Button(top_frame, text="Test",command=self.run_ping)
        dns_button.pack(side='left') 
       
        #Additional Buttons
        open_file_button = Button(bottom_frame, text="Open File", command=self.open_file)
        open_file_button.pack(side='right')
        save_button = Button(bottom_frame, text="Save",command=self.save_output)
        save_button.pack(side='left')
        clear_button = ttk.Button(bottom_frame, text="Clear",command=self.clear_output)
        clear_button.pack(side='left')

        #Menubar label
        file.add_command(label="Open", command=self.open_file)
        file.add_command(label="Save", command=self.save_output)
        file.add_command(label="Clear", command=self.clear_output)        
        file.add_separator()
        file.add_command(label="Exit", command=top.quit)
        menubar.add_cascade(label="File", menu=file)
     
        top.config(menu=menubar)
        top.mainloop()

    #Ping function
    def run_ping(self):
        target = self.entry.get()
        output = subprocess.run(["Ping","-c","5", target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.terminal.insert('end', output.stdout.decode())
    #Nmap function
    def run_nmap(self):
        target = self.entry.get()
        output = subprocess.run(["Nmap", target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.terminal.insert('end', output.stdout.decode())
    #Searchsploit function
    def run_searchsploit(self):
        search_term = self.entry.get()
        output = subprocess.run(["Searchsploit", search_term], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.terminal.insert('end', output.stdout.decode())
    #Netdiscover function
    def run_netdiscover(self):
        ping_term = self.entry.get()
        output = subprocess.run(["netdiscover", ping_term], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.terminal.insert('end', output.stdout.decode())
    #Save file function
    def save_output(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as f:
                f.write(self.terminal.get("1.0", "end"))
                f.write(self.terminal1.get("1.0", "end"))
            tkinter.messagebox.showinfo("Info", "File saved successfully")
        else:

            tkinter.messagebox.showinfo("Error", "Failed to save file.")

    #Open file function
    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text Files", "*.txt"),
                                                          ("All Files", "*.*")])
        try:
            with open(file_path, "r") as file:
                contents = file.read()
                self.terminal1.insert("end", contents)   
        except:
            messagebox.showerror("Error", "Could not open the file.")
    #Clear terminal function
    def clear_output(self):
        self.terminal.delete("1.0", "end")
        self.terminal1.delete("1.0", "end")

#Main Frame
root = Tk()
root.title("NetReconTool")
window = Window(root)
root.mainloop()
