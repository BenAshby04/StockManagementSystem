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
		print("Add New Product")
		print("Delete Product")
		print("Edit Stock Quantity Levels")
		print("List All Products")
		print("Exit")
		print("Commands: Add, Delete, Edit, List, Exit")
		adminMenuInput = input("> ").lower()
		if adminMenuInput == "add":
			addProduct()
		if adminMenuInput == "delete":
			deleteProduct()
		if adminMenuInput == "edit":
			editProduct()
		if adminMenuInput == "list":
			listAllProducts()
		if adminMenuInput == "exit":
			adminMenu = False

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
			idMenu = True
			while itemMenu:
				itemName = input("What is the name of the item? ")
				itemPrice = float(input("What is the price of the item? "))
				# quantity = int(input("How much of this item do you have in stock? "))
				while idMenu:
        
					# barcode = input("What is the barcode of the item (ID that will be used for POS) ")
		
					
					# exists = cur.execute("SELECT * FROM stock WHERE barcode ='{0}'".format(barcode)).fetchone()
					# if exists == None:
						
					#Finds the highest id amount and adds one to it
					# cur.execute("SELECT MAX(id) FROM stock")
					# currentID = cur.fetchone()[0]
					# newID = currentID + 1
					#Inserts the new item into the database table
					cur.execute("INSERT INTO item (itemName, itemPrice) VALUES('{0}','{1}')".format(itemName,itemPrice))
					conn.commit()
					itemMenu = False
					idMenu = False
					# else:
					
						# print("There is a item with that barcode already in the database please try again.")
			
		if menuInput == "exit":
			conn.close()
			return 0

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
                        cur.execute("SELECT id FROM stock WHERE barcode = '{0}'".format(id))
                        idRemoved = cur.fetchone()[0]
                        cur.execute("SELECT * FROM stock")
                        listOfItems = cur.fetchall()
                        for item in listOfItems:
                            if item[0] > idRemoved:
                                cur.execute("UPDATE stock SET id='{0}' WHERE id='{1}'".format(item[0]-1, item[0]))
                        cur.execute("DELETE FROM stock WHERE barcode='{0}'".format(id))
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
    
    cur.execute("SELECT * FROM stock ORDER BY barcode")
    rows = cur.fetchall()
    print()
    print("Products:")
    print("Item Name | Item Price | Barcode")
    for row in rows:
        print("{0} | {2} | {1}".format(row[1], row[4], row[2]))
    conn.close()
    print()
    return 0

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
					cur.execute("SELECT * FROM stock WHERE barcode ='{0}'".format(id))
					
					item = cur.fetchall()[0]
					print("There is currently {0} of {1} left!".format(item[3], item[1]))
					amountToAdd = int(input("How many would you like to add? "))
					newQuantity = item[3] + amountToAdd
					cur.execute("UPDATE stock SET quantity='{0}' WHERE barcode='{1}'".format(newQuantity, id))
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
						totalPrice = totalPrice + itemList[i][2]
					# for item2 in itemList:
					# 	totalPrice =+ item2[2]
					print(totalPrice)
					posAction = False
					newTransaction = transaction(totalPrice, itemList)
					newTransaction.sale()

					
				else:
					try:
						cur.execute("SELECT * FROM stock WHERE barcode='{0}'".format(id))
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
        # ItemID text PRIMARY KEY UNIQUE,
        # aID TEXT GENERATED ALWAYS AS ('IID' || SUBSTR('0000' || ItemID, -4)) STORED,
        cur.execute("""CREATE TABLE item(
			ItemID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   			aID TEXT GENERATED ALWAYS AS ('IID' || SUBSTR('0000' || ItemID, -4)) STORED,
            itemName text,
            itemPrice real)""")
        # CusID text PRIMARY KEY UNIQUE,
        cur.execute("""CREATE TABLE customer(
			CusID text PRIMARY KEY UNIQUE,
            aID TEXT GENERATED ALWAYS AS ('CID' || SUBSTR('0000' || CusID, -4)) STORED,
            fName text,
            lName text,
            address text)""")
            # OrderID text PRIMARY KEY UNIQUE,
        cur.execute("""CREATE TABLE orders(
            OrderID text PRIMARY KEY UNIQUE,
            aID TEXT GENERATED ALWAYS AS ('OID' || SUBSTR('0000' || OrderID, -4)) STORED,
            CusID integer REFERENCES customer(Cus),
            date text,
            disc real,
            FOREIGN KEY(CusID) REFERENCES customer(CusID))""")
        cur.execute("""CREATE TABLE transactions(
            OrderID text,
            TransID text,
            aID TEXT GENERATED ALWAYS AS ('TID' || SUBSTR('0000' || TransID, -4)),
            ItemID text,
            PRIMARY KEY (OrderID, TransID),
            FOREIGN KEY(OrderID) REFERENCES orders(OrderID),
            FOREIGN KEY(ItemID) REFERENCES item(ItemID))""")
        conn.commit()
        conn.close()

        #Add first item to reduce chances of error when scanning through table later on.
        # conn = sqlite3.connect("inventory.db")
        # cur = conn.cursor()
        # print("Please add your first item to the database.")
        # itemName = input("What is the name of the item? ")
        # itemPrice = float(input("What is the price of your item? "))
        # quantity = int(input("How much of this item do you have in stock? "))
        # barcode = input("What is the barcode of the item (ID that will be used for POS) ")

        # cur.execute("INSERT INTO stock VALUES('0', '{0}', '{1}', '{2}', '{3}')".format(itemName, itemPrice, quantity, barcode))	

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