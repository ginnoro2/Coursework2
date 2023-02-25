from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import tkinter.messagebox
from tkinter import messagebox
import subprocess
import os
import logic


class Netrecon:
    def __init__(self, master):
        # Frame
        #top = Toplevel()
        
        top_frame = Frame(master)
        top_frame.pack(side="top", fill="x")
        
        # Menubar
        menubar = Menu(master)
        file = Menu(menubar, tearoff=0)
        
        # Frame for buttons
        bottom_frame = Frame(master)
        bottom_frame.pack(side="bottom", fill="x")
        
        # Display terminal Frame
        main = Frame(master)
        main.pack(fill='both', expand=True)
        self.terminal = Text(main, wrap='word')
        self.terminal.pack(fill='both', expand=True)
        self.terminal1 = Text(main, height=10, width=30, wrap='word')
        self.terminal1.pack(fill='both', expand=True)
        
        # Entry
        self.entry = Entry(master)
        self.entry.pack(side='top', fill='x')
        
        # Function Buttons
        nmap_button = Button(top_frame, text="Network Scan", command=self.nmap)
        nmap_button.pack(side='left')
        searchsploit_button = Button(top_frame, text="Exploit_db", command=self.searchsploit)
        searchsploit_button.pack(side='right')
        discover_button = Button(top_frame, text="Discover", command=self.netdiscover)
        discover_button.pack(side='left')
        dns_button = Button(top_frame, text="Test", command=self.ping)
        dns_button.pack(side='left')
        
        # Additional Buttons
        open_file_button = Button(bottom_frame, text="Open File", command=self.open)
        open_file_button.pack(side='right')
        save_button = Button(bottom_frame, text="Save", command=self.save)
        save_button.pack(side='left')
        clear_button = ttk.Button(bottom_frame, text="Clear", command=self.clear_output)
        clear_button.pack(side='left')
        
        # Menubar label
        file.add_command(label="Open", command=self.open)
        file.add_command(label="Save", command=self.save)
        file.add_command(label="Clear", command=self.clear_output)
        file.add_separator()
        file.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=file)


    def nmap(self):
        target = self.entry.get()
        output = logic.run_nmap(target)
        self.terminal.insert('end', output)

    def ping(self):
        target = self.entry.get()
        output = logic.run_ping(target)
        self.terminal.insert('end', output)

    
    def searchsploit(self):
        target = self.entry.get()
        output = logic.run_searchsploit(target)
        self.terminal.insert('end', output)
   
    def netdiscover(self):
        target = self.entry.get()
        output = logic.run_netdiscover(target)
        self.terminal.insert('end', output)
    
    def save(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as f:
                f.write(self.terminal.get("1.0", "end"))
                f.write(self.terminal1.get("1.0", "end"))
            tkinter.messagebox.showinfo("Info", "File saved successfully")
        else:

            tkinter.messagebox.showinfo("Error", "Failed to save file.")

    #Open file function
    def open(self):
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


root = Tk()
root.title("NetReconTool")
window = Netrecon(root)
root.mainloop()