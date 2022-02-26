from itertools import count
from math import fabs
import sqlite3
from tkinter import INSERT
from typing import Counter

#Classes
class transaction: 
    def __init__(self, totalPrice, items):
        self.items = items
        self.totalPrice = totalPrice
        self.idsUsed = []
    def sale(self):
        items = self.items
        totalPrice = self.totalPrice
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        self.counter = Counter(items)
        textForRecord = ""
        idFound = False
        
        print(self.counter)
            
        for item in items:
            idFound = False
            for id in self.idsUsed:
                # print("id: {0} item[0]: {1}".format(id,item[0]))
                if id == item[0]: idFound = True
            if idFound == False:
                newItem = itemFromDB(item[1], item[2],item[4])
                # textForRecord = textForRecord + "{0} | {1} | {2} \n".format(str(item[1]), str(item[2]), str(item[4]))
                # print(self.counter[item])
                self.idsUsed.append(item[0])
        print("\n\n\n\n")
        for counter in self.counter:
            print("{0} | {1}".format(counter[0], self.counter[counter]))
            textForRecord = textForRecord + "Quantity: {2} | Item Name: {0} | Item Price: {1} | Barcode: {3}\n".format(str(counter[1]),str(counter[2]),str(self.counter[counter]), str(counter[4]))
            
        try:
            transactonNumber = cur.execute("SELECT MAX(transaction_number) FROM transactions").fetchone()[0] +1
        except:
            transactonNumber = 0
            print("Transaction Number Failed")
        
        try:
            cur.execute("INSERT INTO transactions VALUES('{0}', '{1}', '{2}')".format(transactonNumber,textForRecord,totalPrice))
            
            conn.commit()
            conn.close()
        except:
            print("Failed to complete sale")
            
class itemFromDB:
	def __init__(self, itemName, itemPrice, barcode):
		self.itemName = itemName
		self.itemPrice = itemPrice
		self.barcode = barcode
		



#Admin Menus
def admin():
	adminMenu = True
	while adminMenu:
		print("What would you like to do:")
		print("Manage Products")
		print("Manage Customers")
		print("Exit")
		print("Commands: Product, Customer, Exit")
		adminMenuInput = input("> ").lower()
		if adminMenuInput == "product" or adminMenuInput == "p":
			productManagement()
		elif adminMenuInput == "customer" or adminMenuInput == "c":
			customerManagement()
		elif adminMenuInput == "exit":
			adminMenu = False

#Customer Mangement
def customerManagement():
	customerMenu = True
	while customerMenu:
		print("What would you like to do:")
		print("Add a new Customer")
		print("Edit a Customer")
		print("Delete a Customer")
		print("List all Customers")
		print("Exit")
		print("Commands: Add, Edit, Delete, List, Exit")
		customerMenuInput = input("> ").lower()
		if customerMenuInput == "add":
			addCustomer()
		elif customerMenuInput == "edit":
			editCustomer()
		elif customerMenuInput == "delete":
			print("Delte a Customer")
		elif customerMenuInput == "list":
			listAllCustomers()
		elif customerMenuInput == "exit":
			customerMenu = False

def addCustomer():
    addCustomer = True
    conn = sqlite3.connect('inventory.db')
    cur = conn.cursor()
    while addCustomer:
        print("Welcome to the Add Customer menu:")
        print("What would you like to do?")
        print("Add")
        print("Exit")
        print("Commands: add, exit")
        addCustomerInput = input("> ").lower()
        if addCustomerInput == "add":
            customerMenu = True
            while customerMenu:
                print("What is the First Name of the Customer?")
                fName = input().lower()
                print("What is the Last Name of the Customer?")
                lName = input().lower()
                print("What is the Customers Contact Number?")
                contactNumber = input()
                print("What is the address of the Customer?")
                address = input()
                cur.execute("INSERT INTO customer (fName, lName, address, contactNumber) VALUES('{0}', '{1}', '{2}', '{3}')".format(fName.capitalize(),lName.capitalize(),address, contactNumber))
                conn.commit()
                customerMenu = False
        elif addCustomerInput == "exit":
            conn.close()
            addCustomer = False

def editCustomer():
    editCustomerMenu = True
    conn = sqlite3.connect("inventory.db")
    cur = conn.cursor()
    while editCustomerMenu:
        print("What would you like to do?")
        print("Edit the Customers First Name?")
        print("Edit the Customers Last Name?")
        print("Edit the Customers Contact Number?")
        print("Edit the Customers Address?")
        print("Exit")
        print("Commands: fName, lName, number, address, exit")
        menuInput = input("> ").lower()
        #First Name Edit
        if menuInput == "fname" or menuInput == "f":
            fNameMenu = True
            while fNameMenu:
                try:
                    print("What is the customers name that is registered with the account?")
                    oldFName = input("> ").lower()
                    cur.execute("SELECT * FROM customer WHERE fName = '{0}'".format(oldFName.capitalize()))
                    rows = cur.fetchall()
                    print("\nResults:")
                    print("First Name | Last Name | Contact Number | Address | Customer ID")
                    for row in rows:
                        print("{0} | {1} | {2} | {3} | {4}".format(row[2], row[3], row[5], row[4], row [1]))

                except:
                    print("SQL Error: Miss Input")
                
                if len(rows) == 0:
                    print("Results not Found")
                    conn.close()
                    fNameMenu = False
                    namesFound = False
                else: 
                    print()
                    namesFound = True
                
                if namesFound == True:
                    enterID = True
                    while enterID:
                        print("Please Comfirm Details with Customer then enter the Customer ID")
                        customerID = input("> ").upper()
                        if customerID == "EXIT":
                            enterID =False
                        else: 
                            cur.execute("SELECT * FROM customer WHERE CusID = '{0}'".format(customerID))
                            rows = cur.fetchall()
                            if len(rows) > 0:
                                print("What is the customers new first name?")
                                fname = input("> ").lower()
                                cur.execute("UPDATE customer SET fName = '{0}' WHERE CusID = '{1}'".format(fname.capitalize(), customerID))
                                conn.commit()
                                conn.close()
                                enterID = False
                                fNameMenu = False
                            else:
                                print("ID not Found!")

        #Last Name Edit
        elif menuInput == "lname" or menuInput == "l":
            fNameMenu = True
            while fNameMenu:
                try:
                    print("What is the customers first name that is registered with the account?")
                    oldFName = input("> ").lower()
                    cur.execute("SELECT * FROM customer WHERE fName = '{0}'".format(oldFName.capitalize()))
                    rows = cur.fetchall()
                    print("\nResults:")
                    print("First Name | Last Name | Contact Number | Address | Customer ID")
                    for row in rows:
                        print("{0} | {1} | {2} | {3} | {4}".format(row[2], row[3], row[5], row[4], row [1]))

                except:
                    print("SQL Error: Miss Input")
                
                if len(rows) == 0:
                    print("Results not Found")
                    conn.close()
                    fNameMenu = False
                    namesFound = False
                else: 
                    print()
                    namesFound = True
                
                if namesFound == True:
                    enterID = True
                    while enterID:
                        print("Please Comfirm Details with Customer then enter the Customer ID")
                        customerID = input("> ").upper()
                        if customerID == "EXIT":
                            enterID =False
                        else: 
                            cur.execute("SELECT * FROM customer WHERE CusID = '{0}'".format(customerID))
                            rows = cur.fetchall()
                            if len(rows) > 0:
                                print("What is the customers new last name?")
                                lname = input("> ").lower()
                                cur.execute("UPDATE customer SET lName = '{0}' WHERE CusID = '{1}'".format(lname.capitalize(), customerID))
                                conn.commit()
                                conn.close()
                                enterID = False
                                fNameMenu = False
                            else:
                                print("ID not Found!")

        elif menuInput == "number" or menuInput == "n":
            print("Contact Number")
        elif menuInput == "address" or menuInput == "a":
            print("Address")
        elif menuInput == "exit":
            editCustomerMenu = False

def listAllCustomers():
    conn = sqlite3.connect("inventory.db")
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM customer ORDER BY CusID")
    rows = cur.fetchall()
    print()
    print("Customers:")
    print("First Name | Last Name | Contact Number | Address | Customer ID")
    for row in rows:
        print("{0} | {1} | {2} | {3} | {4}".format(row[2], row[3], row[5], row[4], row [1]))
    conn.close()
    print()

#Product Mangement
def productManagement():
	productMenu = True
	while productMenu:
		print("What would you like to do:")
		print("Add New Product")
		print("Delete Product")
		print("Edit Stock Quantity Levels")
		print("List All Products")
		print("Exit")
		print("Commands: Add, Delete, Edit, List, Exit")
		productMenutInput = input("> ").lower()
		if productMenutInput == "add":
			addProduct()
		elif productMenutInput == "delete":
			deleteProduct()
		elif productMenutInput == "edit":
			editProduct()
		elif productMenutInput == "list":
			listAllProducts()
		elif productMenutInput == "exit":
			productMenu = False

def addProduct():
	addMenu = True
	conn = sqlite3.connect("inventory.db")
	cur = conn.cursor()
	while addMenu:
		print("Welcome to the Add Product menu:")
		print("What would you like to do?")
		print("Add")
		print("Exit")
		print("Commands: add, exit")

		menuInput = input("> ").lower()
		if menuInput == "add":
			itemMenu = True
			while itemMenu:
				itemName = input("What is the name of the item? ")
				itemPrice = float(input("What is the price of the item? "))
				quantity = int(input("How much of this item do you have in stock? "))

				#Inserts the new item into the database table
				cur.execute("INSERT INTO item (itemName, itemPrice, quantity) VALUES('{0}','{1}','{2}')".format(itemName,itemPrice, quantity))
				conn.commit()
				itemMenu = False
			
		if menuInput == "exit":
			conn.close()
			addMenu()

def deleteProduct():
    deleteMenu = True
    conn = sqlite3.connect("inventory.db")
    cur = conn.cursor()
    while deleteMenu:
        print("Welcome to the delete menu")
        print("What would you like to do?")
        print("Delete a item")
        print("List all Items")
        print("Exit")
        print("Commands: delete, list, exit")
        menuInput = input("> ").lower()
        if menuInput == "delete":
            listAllProducts()
            idMenu = True
            while idMenu:
                print("Please enter the ID of the item you would like to delete or type 'exit' to go back?")
                id = input("> ")
                if id == "exit":
                    idMenu = False
                else:
                    try:
                        cur.execute("DELETE FROM item WHERE ItemID='{0}'".format(id))
                        print("Item Deleted")
                        idMenu = False
                        conn.commit()
                    except: 
                        print("Not a valid ID")
        elif menuInput == "list":
            listAllProducts()
        elif menuInput == "exit":
            conn.close()
            deleteMenu = False

def listAllProducts():
    conn = sqlite3.connect("inventory.db")
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM item ORDER BY ItemID")
    rows = cur.fetchall()
    print()
    print("Products:")
    print("Item Name | Item Price | Quantity | Item ID")
    for row in rows:
        print("{0} | {1} | {2} | {3}".format(row[2], row[3], row[4], row[1]))
    conn.close()
    print()

def editProduct():
	editMenu = True
	conn = sqlite3.connect("inventory.db")
	cur = conn.cursor()
	while editMenu:
		print("Welcome to the edit stock quantity levels menu:")
		print("What would you like to do?")
		print("Edit")
		print("Exit")
		menuInput = input("> ").lower()
		if menuInput == "edit":
			idMenu = True
			while idMenu:
				listAllProducts()
				print("Please enter the id in full of the item you want to edit (e.g 001)")
				id = input("> ")
				try:
					cur.execute("SELECT * FROM item WHERE ItemID ='{0}'".format(id))
					
					item = cur.fetchall()[0]
					print("There is currently {0} of {1} left!".format(item[4], item[2]))
					amountToAdd = int(input("How many would you like to add? "))
					newQuantity = item[4] + amountToAdd
					cur.execute("UPDATE item SET quantity='{0}' WHERE ItemID='{1}'".format(newQuantity, id))
					conn.commit()
				except:
					print("Item not found")
					
				idMenu = False

		elif menuInput == "exit":
			editMenu = False
			conn.close()

#POS
def pos():
	posMenu = True
	conn = sqlite3.connect("inventory.db")
	cur = conn.cursor()
	while posMenu:
		print("Welcome to the POS Menu")
		print("What would you like to do!")
		print("POS")
		print("Exit")
		print("Commands: POS, Exit")
		posInput = input("> ").lower()
		if posInput == "pos":
			posAction = True	
			itemList = []
			while posAction:
				listAllProducts()
				print("Please type in the ID of the item you want to add to the order? or use one of the commands below.")
				print("Commands: exit, sale ")
				id = input("> ")
				
				if id == "exit":
					posAction = False
				if id == "sale":
					totalPrice = 0.0
					for i in range(len(itemList)):
						totalPrice = totalPrice + itemList[i][3]
					# for item2 in itemList:
					# 	totalPrice =+ item2[2]
					print(totalPrice)
					posAction = False
					# newTransaction = transaction(totalPrice, itemList)
					# newTransaction.sale()

					
				else:
					try:
						cur.execute("SELECT * FROM item WHERE ItemID='{0}'".format(id))
						item = cur.fetchall()[0]
						itemList.append(item)

						print(itemList)

					except:
						print("Item not found")
	
		elif posInput == "exit":
			posMenu = False
    

def checkDatabaseExist():
    try:
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        
        #Create tables in the db
        # ID INTEGER PRIMARY KEY AUTOINCREMENT,
        # aID TEXT GENERATED ALWAYS AS ('IID' || SUBSTR('0000' || ItemID, -4)) STORED,
        cur.execute("""CREATE TABLE item(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
   			ItemID TEXT GENERATED ALWAYS AS ('IID' || SUBSTR('0000' || ID, -4)) STORED,
            itemName text,
            itemPrice real,
            quantity integer)""")
        # CusID text PRIMARY KEY UNIQUE,
        cur.execute("""CREATE TABLE customer(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
            CusID TEXT GENERATED ALWAYS AS ('CID' || SUBSTR('0000' || ID, -4)) STORED,
            fName text,
            lName text,
            address text,
            contactNumber text)""")
            # OrderID text PRIMARY KEY UNIQUE,
        cur.execute("""CREATE TABLE orders(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            OrderID TEXT GENERATED ALWAYS AS ('OID' || SUBSTR('0000' || ID, -4)) STORED,
            CusID integer REFERENCES customer(Cus),
            date text,
            disc real,
            FOREIGN KEY(CusID) REFERENCES customer(CusID))""")
        cur.execute("""CREATE TABLE transactions(
            OrderID text,
            TransID INTEGER,
            aID TEXT GENERATED ALWAYS AS ('TID' || SUBSTR('0000' || TransID, -4)),
            ItemID text,
            PRIMARY KEY (OrderID, TransID),
            FOREIGN KEY(OrderID) REFERENCES orders(OrderID),
            FOREIGN KEY(ItemID) REFERENCES item(ItemID))""")
        conn.commit()
        conn.close()

    except:
        print("Database and table found")

        conn.close()

def main():
	menu = True	
	checkDatabaseExist()
	while menu:
		print("Welcome to the Stock Management System")
		print("What would you like to do!")
		print("POS")
		print("Admin")
		print("View Products")
		print("Exit")
		print("Commands: POS, Admin, View, Exit")
		menuInput = input("> ").lower()

		if menuInput == "pos":
			pos()	
		if menuInput == "admin":
			admin()
		if menuInput == "view":
			listAllProducts()
		if menuInput == "exit":
			menu = False

if __name__ == "__main__":
    main()