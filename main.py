import os
import tkinter as tk
import sqlite3
from turtle import width

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
        rows = cur.fetchall()
        print("Results:")
        for row in rows:
            print("{0},{1},{2},{3},{4}".format(row[2],row[3],row[5],row[4],row[1]))
        conn.close()


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