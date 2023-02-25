from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import tkinter.messagebox
from tkinter import messagebox
import subprocess
import os
import logic


class Window:
    def __init__(self, master):
        # Frame
        self.mainFrame = Frame(master)
        self.mainFrame.pack(side=TOP, padx=100, pady=100)
        
        # Button
        btn_login = Button(self.mainFrame, text="Begin", command=self.Begin, font=('arial', 18), width=35)
        btn_login.grid(row=4, columnspan=2, pady=20)

    def Begin(self):
        self.mainFrame.destroy()
        openwindow = Main()


class Main:
    def __init__(self):
        # Main Login Frame
        Top = Toplevel()
        self.message = StringVar()
        self.username = StringVar()
        self.password = StringVar()
        
        self.LoginFrame = Frame(Top)
        self.LoginFrame.pack(side=TOP, padx=100, pady=100)
        
        # Label Username Password and result display
        lbl_username = Label(self.LoginFrame, text="Username:", font=('arial', 25), bd=18)
        lbl_username.grid(row=1)
        lbl_password = Label(self.LoginFrame, text="Password:", font=('arial', 25), bd=18)
        lbl_password.grid(row=2)
        self.lbl_result1 = Label(self.LoginFrame, text="", font=('arial', 18))
        self.lbl_result1.grid(row=3, columnspan=2)
        
        # Entry frame
        self.username = Entry(self.LoginFrame, font=('arial', 20), width=15)
        self.username.grid(row=1, column=1)
        self.password = Entry(self.LoginFrame, font=('arial', 20), width=15, show="*")
        self.password.grid(row=2, column=1)
        
        # Login Button
        btn_login = Button(self.LoginFrame, text="Login", command=self.login, font=('arial', 18), width=35)
        btn_login.grid(row=4, columnspan=2, pady=20)
        
        # Registry toggle button
        lbl_register = Label(self.LoginFrame, text="Register", fg="Blue", font=('arial', 12))
        lbl_register.grid(row=0, sticky=W)
        lbl_register.bind('<Button-1>', self.ToggleToRegister)


    def login(self):
    
        uname = self.username.get()
        pwd = self.password.get()

        if uname == "" and pwd == "":
            self.lbl_result1.config(text="Please complete the required field!", fg="orange")

        else:
            logic.Login(uname, pwd)
            openwindow = self.recon()
            exit()
                

    def ToggleToRegister(self, event=None):
        self.LoginFrame.destroy()
        openwindow = Register()


    def recon(self):
        os.system('python3 netrecon.py')
        

class Register:
    def __init__(self):
        # Frame
        top = Toplevel()
        
        self.RegisterFrame = Frame(top)
        self.RegisterFrame.pack(side=TOP, padx=100, pady=100)
        
        # Label
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
        
        # Entry
        self.username = Entry(self.RegisterFrame, font=('arial', 20), width=15)
        self.username.grid(row=1, column=1)
        self.password = Entry(self.RegisterFrame, font=('arial', 20), width=15, show="*")
        self.password.grid(row=2, column=1)
        self.firstname = Entry(self.RegisterFrame, font=('arial', 20), width=15)
        self.firstname.grid(row=3, column=1)
        self.lastname = Entry(self.RegisterFrame, font=('arial', 20), width=15)
        self.lastname.grid(row=4, column=1)
        
        # Button
        btn_Register = Button(self.RegisterFrame, text="Register", font=('arial', 18), width=35, command=self.Register)
        btn_Register.grid(row=6, columnspan=2, pady=20)
        
        # Toggle Button
        lbl_login = Label(self.RegisterFrame, text="Login", fg="Blue", font=('arial', 12))
        lbl_login.grid(row=0, sticky=W)
        lbl_login.bind('<Button-1>', self.ToggleToLogin)


    def Register(self):
        username_val = self.username.get()
        password_val = self.password.get()
        firstname_val = self.firstname.get()
        lastname_val = self.lastname.get()

        
        logic.Register(username_val, password_val, firstname_val, lastname_val)
    
        self.lbl_result2.config(text="Successfully Created!", fg="black")



    def ToggleToLogin(self, event=None):
        self.RegisterFrame.destroy()
        Main()
        


# Main Frame
root = Tk()
root.title("Admin Login")
window = Window(root)
root.mainloop()