import os
import tkinter as tk
import sqlite3
from tkinter.messagebox import showinfo
from turtle import width

from telegram import Sticker


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

        ExitBtn = tk.Button(master=buttonsFrame, text="Exit", bg="blue")
        ExitBtn['command'] = self.exit
        ExitBtn.place(x=150, y=250, width=100, height=50)
        
        buttonsFrame.grid(row=0,column=1,sticky="nsew")
        
    def exit(self):
        print("Program Exiting")
        os._exit(0)
    
    def pos(self):
        print("POS Selected")
        POSMenu()
    
    def admin(self):
        print("Admin Selected")
        AdminMenu()
    
class AdminMenu():
    def __init__(self):
        #Window Configuration
        self.win = tk.Toplevel(mainwin)
        self.win.title("Admin Menu")
        self.win.geometry("300x300")
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
        
    def manageCustomer(self):
        print("Manage Customers Selected")
        manageCustomers(self.win)
        
    def manageProduct(self):
        print("Manage Product Selected")
        manageProducts(self.win)

#Product Stuff
class manageProducts():
    def __init__(self,previousWin):
        #Window Configuration
        self.win = tk.Toplevel(previousWin)
        self.win.title("Manage Products")
        self.win.geometry("300x300")
        self.win.rowconfigure(0,weight=1)
        self.win.columnconfigure(1,weight=1)
        
        #Frame Configuration
        manageProductFrame = tk.Frame(master=self.win)
        manageProductFrame.grid(row=0,column=1,sticky="nsew")
        
        #Button Configuration
        exitButton = tk.Button(master=manageProductFrame, text="Exit")
        exitButton['command'] = self.win.destroy
        exitButton.place(x=5,y=5,width=100,height=50)
        
        addProduct = tk.Button(master=manageProductFrame, text="Add a Product")
        addProduct['command'] = self.addProducts
        addProduct.place(x=90,y=70,width=125,height=50)
        
        editProduct = tk.Button(master=manageProductFrame, text="Edit a Product")
        editProduct.place(x=90,y=140,width=125,height=50)
        
        deleteProduct = tk.Button(master=manageProductFrame, text="Delete a Product")
        deleteProduct.place(x=90,y=210,width=125,height=50)
        
    def addProducts(self):
        addProduct(self.win)

class addProduct():
    def __init__(self, previousWindow):
        #Window Configuration
        self.win = tk.Toplevel(previousWindow)
        self.win.title("Add a Product")
        self.win.geometry("500x300")
        self.win.rowconfigure(0,weight=1)
        self.win.columnconfigure(1,weight=1)
        
        #Frame Configuration
        addCustomerFrame = tk.Frame(master=self.win)
        addCustomerFrame.grid(row=0, column=1, sticky="nsew")
        
        #Button Configuration
        exitButton = tk.Button(master= addCustomerFrame,text="Exit")
        exitButton['command'] = self.win.destroy
        exitButton.place(x=5,y=5,width=100, height=50)
        
        submitButton = tk.Button(master= addCustomerFrame, text="Submit")
        submitButton['command'] = self.commitToDB
        submitButton.place(x=395,y=245,width=100,height=50 )
        
        #Label Configuration
        fNameLabel = tk.Label(master=addCustomerFrame, text="Product Name:")
        fNameLabel.place(x=115,y=60, width=100,height=20)
        
        lNameLabel = tk.Label(master=addCustomerFrame, text="Product Price:")
        lNameLabel.place(x=115,y=90, width=100, height=20)
        
        contactLabel = tk.Label(master=addCustomerFrame, text="Quantity:")
        contactLabel.place(x=91, y=120,width=110, height=20)
        
        
        #Textbox Configuration
        self.nameText = tk.Text(master=addCustomerFrame)
        self.nameText.place(x=230,y=60,width=200,height=20)
        
        self.priceText = tk.Text(master=addCustomerFrame)
        self.priceText.place(x=230,y=90,width=200,height=20)
        
        self.quantityText = tk.Text(master=addCustomerFrame)
        self.quantityText.place(x=230,y=120,width=200,height=20)
        

    def commitToDB(self):
        productName = self.nameText.get("1.0", "end").strip()
        productPrice = self.priceText.get("1.0", "end").strip()
        quantity = self.quantityText.get("1.0", "end").strip()
        
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO item (itemName, itemPrice, quantity) VALUES('{0}', '{1}', '{2}') ".format(productName,productPrice,quantity))
        conn.commit()
        conn.close()
        print("Product added: {0}, {1}, {2}".format(productName, productPrice, quantity))

#Customer Stuff
class manageCustomers():
    def __init__(self,previousWindow):
        #Window Configuration
        self.win = tk.Toplevel(previousWindow)
        self.win.title("Manage Customer")
        self.win.geometry("300x300")
        self.win.rowconfigure(0,weight=1)
        self.win.columnconfigure(1,weight=1)
        
        #Frame Configuration
        manageCustomerFrame = tk.Frame(master=self.win)
        manageCustomerFrame.grid(row=0,column=1,sticky="nsew")
        
        #Button Configuration
        exitButton = tk.Button(master=manageCustomerFrame, text="Exit")
        exitButton['command']=self.win.destroy
        exitButton.place(x=5,y=5,width=100,height=50)
        
        addCustomer = tk.Button(master=manageCustomerFrame,text="Add a Customer")
        addCustomer['command'] = self.addCustomer
        addCustomer.place(x=90,y=60,width=125,height=50)
        
        editCustomer = tk.Button(master=manageCustomerFrame,text="Edit a Customer")
        editCustomer['command'] = self.editCustomer
        editCustomer.place(x=90,y=130, width=125,height=50)
        
        deleteCustomer = tk.Button(master=manageCustomerFrame,text="Delete a Customer")
        deleteCustomer.place(x=90,y=200,width=125,height=50)
    def addCustomer(self):
        addCustomers(self.win)
    def editCustomer(self):
        editCustomers(self.win)

class addCustomers():
    def __init__(self, previousWindow):
        #Window Configuration
        self.win = tk.Toplevel(previousWindow)
        self.win.title("Add a Customer")
        self.win.geometry("500x300")
        self.win.rowconfigure(0,weight=1)
        self.win.columnconfigure(1,weight=1)
        
        #Frame Configuration
        addCustomerFrame = tk.Frame(master=self.win)
        addCustomerFrame.grid(row=0, column=1, sticky="nsew")
        
        #Button Configuration
        exitButton = tk.Button(master= addCustomerFrame,text="Exit")
        exitButton['command'] =self.win.destroy
        exitButton.place(x=5,y=5,width=100, height=50)
        
        submitButton = tk.Button(master= addCustomerFrame, text="Submit")
        submitButton['command'] =self.commitToDB
        submitButton.place(x=395,y=245,width=100,height=50 )
        
        #Label Configuration
        fNameLabel = tk.Label(master=addCustomerFrame, text="First Name:")
        fNameLabel.place(x=115,y=60, width=100,height=20)
        
        lNameLabel = tk.Label(master=addCustomerFrame, text="Last Name:")
        lNameLabel.place(x=115,y=90, width=100, height=20)
        
        contactLabel = tk.Label(master=addCustomerFrame, text="Contact Number:")
        contactLabel.place(x=91, y=120,width=110, height=20)
        
        addressLabel = tk.Label(master=addCustomerFrame, text="Address:")
        addressLabel.place(x=120, y=150, width=100,height=20)
        
        #Textbox Configuration
        self.fNameText = tk.Text(master=addCustomerFrame)
        self.fNameText.place(x=230,y=60,width=200,height=20)
        
        self.lNameText = tk.Text(master=addCustomerFrame)
        self.lNameText.place(x=230,y=90,width=200,height=20)
        
        self.contactText = tk.Text(master=addCustomerFrame)
        self.contactText.place(x=230,y=120,width=200,height=20)
        
        self.addressText = tk.Text(master=addCustomerFrame)
        self.addressText.place(x=230,y=150,width=200,height=20)
        
    def commitToDB(self):
        fName = self.fNameText.get("1.0", "end").strip()
        lName = self.lNameText.get("1.0", "end").strip()
        contactNum = self.contactText.get("1.0", "end").strip()
        address = self.addressText.get("1.0","end").strip()
        
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO customer (fName, lName, address, contactNumber) VALUES('{0}', '{1}', '{2}', '{3}') ".format(fName,lName, address,contactNum))
        conn.commit()
        conn.close()
        print("Customer added: {0}, {1}, {2}, {3}".format(fName, lName, contactNum, address))

class editCustomers():
    def __init__(self, previousWindow):
        #Window Configuration
        self.win = tk.Toplevel(previousWindow)
        self.win.title("Edit a Customer")
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
            SelectProfile(self.win, profiles)

class SelectProfile():
    def __init__(self,previousWindow, possibleProfiles):
        #Window Configuration
        self.profiles = possibleProfiles
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
        editCustomerProfile(self.win, self.profiles[self.currentProfile])

    
class editCustomerProfile():
    def __init__(self, previousWin,currentProfiles):
        #Window Configuration
        self.profile = currentProfiles
        self.win = tk.Toplevel(previousWin)
        self.win.title("Edit the Custoemr Profile")
        self.win.geometry("500x300")
        self.win.rowconfigure(0,weight=1)
        self.win.columnconfigure(1,weight=1)
        
        #Frame Configuration
        editCustomerFrame = tk.Frame(master=self.win)
        editCustomerFrame.grid(row=0, column=1, sticky="nsew")
        
        #Button Configuration
        exitButton = tk.Button(master= editCustomerFrame,text="Exit")
        exitButton['command'] =self.win.destroy
        exitButton.place(x=5,y=5,width=100, height=50)
        
        submitButton = tk.Button(master= editCustomerFrame, text="Submit")
        submitButton['command'] = self.commitToDB
        submitButton.place(x=395,y=245,width=100,height=50 )
        
        #Label Configuration
        fNameLabel = tk.Label(master=editCustomerFrame, text="First Name:")
        fNameLabel.place(x=115,y=60, width=100,height=20)
        
        lNameLabel = tk.Label(master=editCustomerFrame, text="Last Name:")
        lNameLabel.place(x=115,y=90, width=100, height=20)
        
        contactLabel = tk.Label(master=editCustomerFrame, text="Contact Number:")
        contactLabel.place(x=91, y=120,width=110, height=20)
        
        addressLabel = tk.Label(master=editCustomerFrame, text="Address:")
        addressLabel.place(x=120, y=150, width=100,height=20)
        
        instructionLabel = tk.Label(master=editCustomerFrame,text="Edit This Customer's Profile then press \nSubmit to commit changes!")
        instructionLabel.place(x=105,y=5, width=300,height=40)
        
        #Textbox Configuration
        self.fNameText = tk.Text(master=editCustomerFrame)
        self.fNameText.place(x=230,y=60,width=200,height=20)
        
        self.lNameText = tk.Text(master=editCustomerFrame)
        self.lNameText.place(x=230,y=90,width=200,height=20)
        
        self.contactText = tk.Text(master=editCustomerFrame)
        self.contactText.place(x=230,y=120,width=200,height=20)
        
        self.addressText = tk.Text(master=editCustomerFrame)
        self.addressText.place(x=230,y=150,width=200,height=20)
        
        self.loadDataFromDB()
        
    def loadDataFromDB(self):
        fName = self.profile[2]
        lName = self.profile[3]
        address = self.profile[4]
        contact = self.profile[5]
        
        self.fNameText.insert("1.0", fName)
        self.lNameText.insert("1.0",lName)
        self.addressText.insert("1.0",address)
        self.contactText.insert("1.0",contact)
    
    def commitToDB(self):
        fName = self.fNameText.get("1.0", "end").strip()
        lName = self.lNameText.get("1.0", "end").strip()
        address = self.addressText.get("1.0", "end").strip()
        contact = self.contactText.get("1.0", "end").strip()
        customerID = self.profile[1]
        
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        cur.execute("UPDATE customer SET fName = '{0}', lName = '{1}', address = '{2}', contactNumber = '{3}' WHERE CusID = '{4}'".format(fName,lName,address,contact,customerID))
        conn.commit()
        conn.close()
        print("Customer updated:")
        print("{0}, {1}, {2}, {3}".format(fName,lName,address,contact))
#POS Stuff
class POSMenu():
    def __init__(self):
        #Window Configuration
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


def checkDatabaseExist():
    try:
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        
        #Create tables in the db
        cur.execute("""CREATE TABLE item(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ItemID TEXT GENERATED ALWAYS AS ('IID' || SUBSTR('0000' || ID, -4)) STORED,
            itemName text,
            itemPrice real,
            quantity integer)""")
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