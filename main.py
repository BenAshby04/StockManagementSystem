from itertools import count
from math import fabs
import sqlite3
from typing import Counter
from datetime import date

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
			deleteCustomer()
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
    
    while editCustomerMenu:
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
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
                    namesFound = False
                
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
            lNameMenu = True
            while lNameMenu:
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
                    namesFound = False
                
                if len(rows) == 0:
                    print("Results not Found")
                    conn.close()
                    lNameMenu = False
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
                                lNameMenu = False
                            else:
                                print("ID not Found!")
        #Number edit menu
        elif menuInput == "number" or menuInput == "n":
            numberMenu = True
            while numberMenu:
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
                    namesFound = False
                
                if len(rows) == 0:
                    print("Results not Found")
                    conn.close()
                    numberMenu = False
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
                                print("What is the customers new Contact Number?")
                                number = input("> ").lower()
                                cur.execute("UPDATE customer SET contactNumber = '{0}' WHERE CusID = '{1}'".format(number.capitalize(), customerID))
                                conn.commit()
                                conn.close()
                                enterID = False
                                numberMenu = False
                            else:
                                print("ID not Found!")

        #Address edit menu
        elif menuInput == "address" or menuInput == "a":
            addressMenu = True
            while addressMenu:
                try:
                    conn = sqlite3.connect("inventory.db")
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
                    namesFound = False
                
                if len(rows) == 0:
                    print("Results not Found")
                    conn.close()
                    addressMenu = False
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
                                print("What is the customers new address?")
                                address = input("> ").lower()
                                cur.execute("UPDATE customer SET address = '{0}' WHERE CusID = '{1}'".format(address.capitalize(), customerID))
                                conn.commit()
                                conn.close()
                                enterID = False
                                addressMenu = False
                            else:
                                print("ID not Found!")

        elif menuInput == "exit":
            editCustomerMenu = False

def deleteCustomer():
    deleteCustomerMenu = True
    conn = sqlite3.connect("inventory.db")
    cur = conn.cursor()
    while deleteCustomerMenu:
        print("What would you like to do?")
        print("Delete a Customer")
        print("Exit")
        print("Commands: Delete, Exit")
        menuInput = input("> ").lower()
        if menuInput == "delete" or menuInput == "d":
            print("What is the Customer's First Name?")
            cusFName = input("> ").lower()
            cur.execute("SELECT * FROM customer WHERE fName = '{0}'".format(cusFName.capitalize()))
            rows = cur.fetchall()
            print("\nResults")
            print("First Name | Last Name | Contact Number | Address | Customer ID")

            for row in rows:
                print("{0} | {1} | {2} | {3} | {4}".format(row[2], row[3], row[5], row[4], row [1]))

            if len(rows) == 0:
                print("No Results found")
                conn.close()
                deleteCustomerMenu = False
                namesFound = False
            else:
                print()
                namesFound = True

            if namesFound == True:
                enterID = True
                while enterID:
                    print("Please Confirm Details with Customer and enter the Customer ID")
                    customerID = input("> ").upper()
                    if customerID == "EXIT":
                        namesFound = False
                    else:
                        cur.execute("SELECT * FROM customer WHERE CusID = '{0}'".format(customerID))
                        rows = cur.fetchone()
                        if len(rows) > 0:
                            deleteMenu = True
                            while deleteMenu:
                                print("Are you sure you want to delete {0}'s account?".format(rows[2]))
                                print("Type 'DELETE' if you want to delete the account!")
                                print("If you want to go back type 'Exit'")
                                print("WARNING: Once account is deleted you will not be able to recover the account!")
                                delete = input("> ")
                                if delete == "DELETE":
                                    cur.execute("DELETE FROM customer WHERE CusID = '{0}'".format(customerID))
                                    conn.commit()
                                    conn.close()
                                    deleteMenu = False
                                    enterID = False
                                    deleteCustomerMenu = False
                                elif delete.lower() == "exit":
                                    deleteMenu = False
                                    enterID = False
                                    deleteCustomerMenu = False
        elif menuInput == "exit":
            deleteCustomerMenu = False                                                         

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
			addMenu = False

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
            lookingForAccount = True
            while lookingForAccount:
                print("Does the Customer have a account?")
                print("Commands: Yes, No, Exit")
                account = input("> ").lower()
                if account == "yes" or account == "y":
                    #Continue Transaction
                    print("What is the customers first name?")
                    fName = input("> ").lower()
                    cur.execute("SELECT * FROM customer WHERE fName = '{0}'".format(fName.capitalize()))
                    rows = cur.fetchall()
                    print("First Name | Last Name | Contact Number | Address | Customer ID")
                    for row in rows:
                        print("{0} | {1} | {2} | {3} | {4}".format(row[2], row[3], row[5], row[4], row [1]))
                    print("Confirm the Details with the customer, then enter their Customer ID")
                    customerID = input("> ").upper()
                    cur.execute("SELECT * FROM customer WHERE CusID = '{0}'".format(customerID))
                    Customer = cur.fetchone()
                    today = date.today()
                    cur.execute("INSERT INTO orders (CusID, date) VALUES ('{0}', '{1}')".format(Customer[1], today.strftime("%d/%m/%Y")))
                    conn.commit()
                    cur.execute("SELECT * FROM orders WHERE OrderID = (SELECT MAX(OrderID) FROM orders)")
                    orderID = cur.fetchone()
                    
                    #Start adding items to transaction
                    addTransaction = True
                    subtotal = 0.0
                    while addTransaction:
                        listAllProducts()
                        print("Current SubTotal: {0}".format(subtotal))
                        print("Please enter a Item ID or type 'exit' to go back")
                        itemID = input("> ").upper()
                        
                        if itemID == "EXIT":
                            cur.execute("UPDATE orders SET subtotal = '{0}' WHERE OrderID = '{1}'".format(subtotal,orderID[1]))
                            conn.commit()
                            addTransaction = False
                        else:
                            try:
                                cur.execute("SELECT * FROM item WHERE itemID = '{0}'".format(itemID))
                                item = cur.fetchone()
                                
                                if len(item) > 0:
                                    cur.execute("INSERT INTO transactions (OrderID, ItemID) VALUES ('{0}', '{1}')".format(orderID[1],item[1]))
                                    subtotal = subtotal + item[3]
                                    conn.commit()
                            except:
                                print("Error: Item Not Found")
                        
                elif account == "no" or account == "n":
                    #Create a account
                    addCustomer()
                elif account == "exit" or account == "e":
                    lookingForAccount = False
            
        elif posInput == "exit":
            posMenu = False
    

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