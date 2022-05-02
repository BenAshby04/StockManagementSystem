import os
import tkinter as tk
import sqlite3
from tkinter.messagebox import showinfo
from customer import *
from product import *
from pos import *
from folder import *


currentProfile = []
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        #Window Configure
        self.title("Main Menu")
        self.geometry("400x400")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        
        buttonsFrame = tk.Frame(master=self)
        
        POSBtn = tk.Button(master=buttonsFrame, text="POS")
        POSBtn['command'] = self.pos
        POSBtn.place(x=150,y=100,width=100,height=50)
        
        AdminBtn = tk.Button(master=buttonsFrame, text="Admin")
        AdminBtn['command'] = self.admin
        AdminBtn.place(x=150 , y=175, width=100, height =50)

        ExitBtn = tk.Button(master=buttonsFrame, text="Exit")
        ExitBtn['command'] = self.exit
        ExitBtn.place(x=150, y=250, width=100, height=50)
        
        buttonsFrame.grid(row=0,column=1,sticky="nsew")
        
    def exit(self):
        print("Program Exiting")
        os._exit(0)
    
    def pos(self):
        print("POS Selected")
        POSMenu(mainwin)
    
    def admin(self):
        print("Admin Selected")
        AdminMenu()
    
class AdminMenu():
    def __init__(self):
        #Window Configuration
        self.win = tk.Toplevel(mainwin)
        self.win.title("Admin Menu")
        self.win.geometry("300x350")
        self.win.rowconfigure(0, weight=1)
        self.win.columnconfigure(1, weight=1)
        
        #Frame Configuration
        adminMenuFrame = tk.Frame(master=self.win)
        adminMenuFrame.grid(row=0, column=1, sticky="nsew")
        
        #Button Configuration
        exitButton = tk.Button(master=adminMenuFrame, text="Exit")
        exitButton['command'] = self.win.destroy
        exitButton.place(x=5,y=5, width=100, height=50)
        
        customerButton = tk.Button(master=adminMenuFrame, text="Manage Customers")
        customerButton['command'] = self.manageCustomer
        customerButton.place(x=85, y=100, width=130, height=50)
        
        productButton = tk.Button(master=adminMenuFrame, text="Manage Products")
        productButton['command']=self.manageProduct
        productButton.place(x=85,y=175, width=130, height=50)  
        
        folderButton = tk.Button(master=adminMenuFrame, text="Manage Folders")
        folderButton['command'] = self.manageFolder
        folderButton.place(x=85, y=250, width=130, height=50)
        
    def manageCustomer(self):
        print("Manage Customers Selected")
        manageCustomers(self.win)
        
    def manageProduct(self):
        print("Manage Product Selected")
        manageProducts(self.win)
    
    def manageFolder(self):
        print("Manage Folders Selected")
        Folder(self.win)



        

def checkDatabaseExist():
    try:
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        
        #Create tables in the db
        cur.execute("""CREATE TABLE folders(
            FolderID TEXT GENERATED ALWAYS AS ('FID' || SUBSTR('0000' || ID, -4)),
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            FolderName text)
            """)
        cur.execute("""CREATE TABLE item(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ItemID TEXT GENERATED ALWAYS AS ('IID' || SUBSTR('0000' || ID, -4)) STORED,
            itemName text,
            itemPrice real,
            quantity integer,
            FolderID text,
            FOREIGN KEY(FolderID) REFERENCES folder(FolderID))""")
        cur.execute("""CREATE TABLE customer(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            CusID TEXT GENERATED ALWAYS AS ('CID' || SUBSTR('0000' || ID, -4)) STORED,
            fName text,
            lName text,
            address text,
            contactNumber text)""")
        cur.execute("""CREATE TABLE orders(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            OrderID TEXT GENERATED ALWAYS AS ('OID' || SUBSTR('0000' || ID, -4)) STORED,
            CusID integer REFERENCES customer(Cus),
            date text,
            subtotal real,
            FOREIGN KEY(CusID) REFERENCES customer(CusID))""")
        cur.execute("""CREATE TABLE transactions(
            OrderID text,
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            TransID TEXT GENERATED ALWAYS AS ('TID' || SUBSTR('0000' || ID, -4)),
            ItemID text,
            FOREIGN KEY(OrderID) REFERENCES orders(OrderID),
            FOREIGN KEY(ItemID) REFERENCES item(ItemID))""")
        
        conn.commit()
        conn.close()

    except:
        print("Database and table found")

        conn.close()

if __name__ == "__main__":
    checkDatabaseExist()
    mainwin = App()
    mainwin.mainloop()