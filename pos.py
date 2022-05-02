import math
import sqlite3
from sys import getprofile
import tkinter as tk
from tkinter.messagebox import showinfo
import os
from customer import *
from datetime import date

#POS Stuff
customerProfileID = None

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
        self.win.geometry("900x600")
        self.win.rowconfigure(0, weight=1)
        self.win.columnconfigure(1, weight=1)
        
        #Frame Configuration
        self.posButtonFrame = tk.Frame(master=self.win)
        self.posButtonFrame.grid(row=0,column=1,sticky="nsew")
        
        #Button Configuration
        exitButton = tk.Button(master=self.posButtonFrame, text="Exit")
        exitButton['command'] = self.win.destroy
        exitButton.place(x=5,y=5,width=100,height=50)
        
        subtotalButton = tk.Button(master=self.posButtonFrame,text="Subtotal")
        subtotalButton['command'] = self.subtotalOrder
        subtotalButton.place(x=350,y=545, width=100, height=50)
        
        #Label Configuration
        self.subtotalLabel = tk.Label(master=self.posButtonFrame, text="Subtotal: {0}".format(self.subtotal), anchor="w")
        self.subtotalLabel.place(x=5, y=570, width=150, height=20)
        
        #Folder Button
        
        
        #Product Button Configuration
        X = 55
        Y = 75
        xAdd = X +100 + 10
        yAdd = Y  + 10
        amountOfItems = len(self.items)
        pages = math.ceil(amountOfItems / 20)
        currentPage = 1 
        # loadButtons(currentPage)
        for item in self.items:
            self.itemButtom.append(tk.Button(master=self.posButtonFrame,text=item[2]))
            self.itemButtom[self.currentItem]['command'] = lambda itemFunc = item: self.addItemToOrder(itemFunc)
            self.itemButtom[self.currentItem].place(x=X,y=Y,width=100,height=50)
            X = X + xAdd
            if X >= 690:
                X = 55
                Y = Y + yAdd
                
            self.currentItem = self.currentItem + 1
        def loadButtons(self, currentPage):
            for item in self.items:
                if currentPage == 1:
                    if self.items.index(item) >= (currentPage * 20):
                        break
                    self.itemButtom.append(tk.Button(master=self.posButtonFrame,text=item[2]))
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
        #Figure out how to debug this
        SubtotalOrder(self.win, self.orderList, self.subtotal)
        # conn = sqlite3.connect("inventory.db")
        # cur = conn.cursor()
        # print(customerProfileID)
        # today = date.today()
        # cur.execute("INSERT INTO orders (cusID, date, subtotal) VALUES ('{0}', '{1}', '{2}')".format(customerProfileID, today.strftime("%d/%m/%Y"), self.subtotal))
        # cur.execute("SELECT * FROM orders WHERE OrderID = (SELECT MAX(OrderID) FROM orders)")
        # orderID = cur.fetchone()
        
        # for items in self.orderList:
        #     cur.execute("INSERT INTO transactions (OrderID, ItemID) VALUES ('{0}', '{1}')".format(orderID[1], items[1]))
            
        # conn.commit()
        # conn.close()
        
class SubtotalOrder():
    def __init__(self, previousWindow, orderlist, subtotal):
        self.orderList = orderlist
        self.subtotal = subtotal
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
            SelectProfilePOS(self.win, profiles, "subtotal", self.orderList, self.subtotal)
  

class SelectProfilePOS():
    def __init__(self,previousWindow, possibleProfiles, function, orderlist, subtotal):
        self.orderList = orderlist
        self.subtotal = subtotal
        #Window Configuration
        self.profiles = possibleProfiles
        self.function = function
        self.currentProfile = 0
        self.win = tk.Toplevel(previousWindow)
        self.win.title("Select a Profile")
        self.win.geometry("500x300")
        self.win.rowconfigure(0,weight=1)
        self.win.columnconfigure(1, weight=1)
        
        #Frame Configuration
        selectProfileFrame = tk.Frame(master=self.win)
        selectProfileFrame.grid(row=0,column=1,sticky="nsew")
        
        #Button Configuration
        exitButton = tk.Button(master=selectProfileFrame, text="Exit")
        exitButton['command'] = self.win.destroy
        exitButton.place(x=5,y=5,width=100,height=50)
        
        selectButton = tk.Button(master=selectProfileFrame, text="Submit")
        selectButton['command'] = self.submit
        selectButton.place(x=200, y=245,width=100, height=50)
        
        nextButton = tk.Button(master=selectProfileFrame, text="Next")
        nextButton['command'] = self.nextProfile
        nextButton.place(x=395, y=175, width=100,height=50)
        
        previousButton = tk.Button(master=selectProfileFrame, text="Previous")
        previousButton['command'] = self.previousProfile
        previousButton.place(x=5, y=175, width=100, height=50)
        
        #Label Configuration
        fNameLabel = tk.Label(master=selectProfileFrame, text="First Name:")
        fNameLabel.place(x=115,y=60, width=100,height=20)
        
        lNameLabel = tk.Label(master=selectProfileFrame, text="Last Name:")
        lNameLabel.place(x=115,y=90, width=100, height=20)
        
        contactLabel = tk.Label(master=selectProfileFrame, text="Contact Number:")
        contactLabel.place(x=91, y=120,width=110, height=20)
        
        addressLabel = tk.Label(master=selectProfileFrame, text="Address:")
        addressLabel.place(x=120, y=150, width=100,height=20)
        
        #Textbox Configuration
        self.fNameText = tk.Text(master=selectProfileFrame)
        self.fNameText.place(x=230,y=60,width=200,height=20)
        
        self.lNameText = tk.Text(master=selectProfileFrame)
        self.lNameText.place(x=230,y=90,width=200,height=20)
        
        self.contactText = tk.Text(master=selectProfileFrame)
        self.contactText.place(x=230,y=120,width=200,height=20)
        
        self.addressText = tk.Text(master=selectProfileFrame)
        self.addressText.place(x=230,y=150,width=200,height=20)
        
        self.firstProfile()
        print("Current Profile: " + str(self.currentProfile))
        
    def firstProfile(self):
        #This functions loads the first profile from the SQL Query into the textboxes on screen
        firstProfile = self.profiles[0]
        self.fNameText.insert("1.0", firstProfile[2])
        self.lNameText.insert("1.0", firstProfile[3])
        self.addressText.insert("1.0", firstProfile[4])
        self.contactText.insert("1.0", firstProfile[5])
        
    def nextProfile(self):
        #This function will load the next profile in the list
        #If it reaches the end of the list it will loop back around to the first profile.
        
        #Makes the Textboxes Blank
        self.fNameText.delete("1.0",'end')
        self.lNameText.delete("1.0",'end')
        self.addressText.delete("1.0",'end')
        self.contactText.delete("1.0",'end')
        
        # print(len(self.profiles))
        self.currentProfile = self.currentProfile +1
        
        #Checks if self.currentProfile goes over the number of profiles found and if it is sets it back to 0
        if (self.currentProfile + 1) > len(self.profiles):
            self.currentProfile = 0
        profile = self.profiles[self.currentProfile]
        
        #Updates textboxes
        self.fNameText.insert("1.0", profile[2])
        self.lNameText.insert("1.0", profile[3])
        self.addressText.insert("1.0", profile[4])
        self.contactText.insert("1.0", profile[5])
        
    def previousProfile(self):
        #This functions will the load the previous profile in the list
        #If it is the first item in the list it will loop to the last profile in the list
        
        #Makes the Textboxes Blank
        self.fNameText.delete("1.0",'end')
        self.lNameText.delete("1.0",'end')
        self.addressText.delete("1.0",'end')
        self.contactText.delete("1.0",'end')
        
        # print(len(self.profiles))
        self.currentProfile = self.currentProfile - 1
        #Checks if self.currentProfile is below 0 if it is it will set it to the max of the list
        if(self.currentProfile) < 0:
            self.currentProfile = (len(self.profiles)-1)
        #Grabs profile from list
        profile = self.profiles[self.currentProfile]
        #Updates textboxes
        self.fNameText.insert("1.0", profile[2])
        self.lNameText.insert("1.0", profile[3])
        self.addressText.insert("1.0", profile[4])
        self.contactText.insert("1.0", profile[5])
    
    def submit(self):
        #Goto edit values to make the changes to that profile.
        print(self.profiles[self.currentProfile])
        if self.function == "edit":
            editCustomerProfile(self.win, self.profiles[self.currentProfile])
        elif self.function == "delete":
            deleteProfile(self.win,self.profiles[self.currentProfile])
        elif self.function == "subtotal":
            getProfile(self.profiles[self.currentProfile][1], self.orderList, self.subtotal)
        else:
            showinfo("Error", "Error: class: SelectProfile, Function:submit, self.function is not 'edit' or 'delete'")
    
def getProfile(profile, orderlist, subtotal):
    customerProfileID = profile
    conn = sqlite3.connect("inventory.db")
    cur = conn.cursor()
    print(customerProfileID)
    today = date.today()
    cur.execute("INSERT INTO orders (cusID, date, subtotal) VALUES ('{0}', '{1}', '{2}')".format(customerProfileID, today.strftime("%d/%m/%Y"), subtotal))
    cur.execute("SELECT * FROM orders WHERE OrderID = (SELECT MAX(OrderID) FROM orders)")
    orderID = cur.fetchone()

    for items in orderlist:
        itemID = items[1]
        cur.execute("INSERT INTO transactions (OrderID, ItemID) VALUES ('{0}', '{1}')".format(orderID[1], items[1]))
        conn.commit()
        cur.execute("SELECT * FROM item WHERE ItemID = '{0}'".format(items[1]))
        quantityObject = cur.fetchone()
        newQuantity = quantityObject[4] - 1
        cur.execute("UPDATE item SET quantity = '{0}' WHERE ItemID = '{1}'".format(newQuantity, itemID))
        
    conn.commit()
    conn.close()