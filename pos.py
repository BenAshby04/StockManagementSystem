import sqlite3
import tkinter as tk
from tkinter.messagebox import showinfo
import os
from customer import *
from datetime import date

#POS Stuff
class POSMenu():
    def __init__(self, previousWin):
        #Window Configuration
        self.detectItems()
        self.currentItem = 0
        print(self.amountOfItems)
        self.itemButtom = []
        self.subtotal = 0.0
        self.orderList = []
        
        self.win = tk.Toplevel(previousWin)
        self.win.title("POS")
        self.win.geometry("800x600")
        self.win.rowconfigure(0, weight=1)
        self.win.columnconfigure(1, weight=1)
        
        #Frame Configuration
        posButtonFrame = tk.Frame(master=self.win)
        posButtonFrame.grid(row=0,column=1,sticky="nsew")
        
        #Button Configuration
        exitButton = tk.Button(master=posButtonFrame, text="Exit")
        exitButton['command'] = self.win.destroy
        exitButton.place(x=5,y=5,width=100,height=50)
        
        subtotalButton = tk.Button(master=posButtonFrame,text="Subtotal")
        subtotalButton['command'] = self.subtotalOrder
        subtotalButton.place(x=350,y=545, width=100, height=50)
        
        #Label Configuration
        self.subtotalLabel = tk.Label(master=posButtonFrame, text="Subtotal: {0}".format(self.subtotal), anchor="w")
        self.subtotalLabel.place(x=5, y=570, width=150, height=20)
        
        
        #Product Button Configuration
        X = 55
        Y = 75
        xAdd = X +100 + 10
        yAdd = Y  + 10
        for item in self.items:
            self.itemButtom.append(tk.Button(master=posButtonFrame,text=item[2]))
            self.itemButtom[self.currentItem]['command'] = lambda itemFunc = item: self.addItemToOrder(itemFunc)
            self.itemButtom[self.currentItem].place(x=X,y=Y,width=100,height=50)
            X = X + xAdd
            if X >= 690:
                X = 55
                Y = Y + yAdd
                
            self.currentItem = self.currentItem + 1
        
    def addItemToOrder(self, item):
        self.orderList.append(item)
        print(item)
        self.subtotal = self.subtotal + item[3]
        self.subtotalLabel.configure(text="Subtotal: {0}".format(self.subtotal))
        print(self.orderList)
        print(self.subtotal)
        
    def detectItems(self):
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM item")
        
        self.items = cur.fetchall()
        self.amountOfItems = len(self.items)
    
    def subtotalOrder(self):
        profile = SubtotalOrder(self.win)
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        
        today = date.today()
        cur.execute("INSERT INTO orders (cusID, date, subtotal) VALUES ('{0}', '{1}', '{2}')".format(profile, today.strftime("%d/%m/%Y"), self.subtotal))
        cur.execute("SELECT * FROM orders WHERE OrderID = (SELECT MAX(OrderID) FROM orders)")
        orderID = cur.fetchone()
        
        for items in self.orderList:
            cur.execute("INSERT INTO transactions (OrderID, ItemID) VALUES ('{0}', '{1}')".format(orderID, items[1]))
            conn.commit()
            
        
class SubtotalOrder():
    def __init__(self, previousWindow):
        #Window Configuration
        self.win = tk.Toplevel(previousWindow)
        self.win.title("Search for a Customer")
        self.win.geometry("500x300")
        self.win.rowconfigure(0, weight=1)
        self.win.columnconfigure(1, weight=1)
        
        #Frame Configuration
        editCustomerFrame = tk.Frame(master=self.win)
        editCustomerFrame.grid(row=0,column=1, sticky="nsew")
        
        #Label Configuration
        fNameLabel = tk.Label(master=editCustomerFrame, text="First Name:")
        fNameLabel.place(x=115, y=60, width=100, height=20)
        
        lNameLabel = tk.Label(master=editCustomerFrame, text="Last Name:")
        lNameLabel.place(x=115, y=90, width=100, height=20)
        
        #Button Configuration
        exitButton = tk.Button(master=editCustomerFrame, text="Exit")
        exitButton['command'] = self.win.destroy
        exitButton.place(x=5,y=5, width=100,height=50)
        
        searchButton = tk.Button(master=editCustomerFrame, text="Search")
        searchButton['command'] = self.findDataDB
        searchButton.place(x=200,y=240, width=100,height=50)
        
        #Textbox Configuration
        self.fNameText = tk.Text(master=editCustomerFrame)
        self.fNameText.place(x=230, y=60, width=200,height=20)
        
        self.lNameText = tk.Text(master= editCustomerFrame)
        self.lNameText.place(x=230,y=90,width=200,height=20)

    def findDataDB(self):
        fName = self.fNameText.get("1.0", "end").strip()
        lName = self.lNameText.get("1.0", "end").strip()
        
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM customer WHERE fName = '{0}' OR lName = '{1}'".format(fName, lName))
        profiles = cur.fetchall()
        print("Results:")
        for profile in profiles:
            print("{0},{1},{2},{3},{4}".format(profile[2],profile[3],profile[5],profile[4],profile[1]))
        conn.close()
        if len(profiles) == 0:
            showinfo(title="Warning", message="There isn't any profiles with these details!")
        else:
            profile = SelectProfile(self.win, profiles, "subtotal")
            return profile
            self.win.destroy()

