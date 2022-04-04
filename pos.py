import sqlite3
import tkinter as tk
from tkinter.messagebox import showinfo
import os

#POS Stuff
class POSMenu():
    def __init__(self):
        #Window Configuration
        self.detectItems()
        self.currentItem = 0
        print(self.amountOfItems)
        self.itemButtom = []
        self.subtotal = 0.0
        self.orderList = []
        
        self.win = tk.Toplevel(mainwin)
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

