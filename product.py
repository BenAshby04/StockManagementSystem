import sqlite3
import tkinter as tk
from tkinter.messagebox import showinfo
import os

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
        editProduct['command'] = self.editProduct
        editProduct.place(x=90,y=140,width=125,height=50)
        
        deleteProduct = tk.Button(master=manageProductFrame, text="Delete a Product")
        deleteProduct['command'] = self.deleteProduct
        deleteProduct.place(x=90,y=210,width=125,height=50)
        
    def addProducts(self):
        addProduct(self.win)
    def editProduct(self):
        editProducts(self.win)
    def deleteProduct(self):
        DeleteProductsMenu(self.win)

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
        self.win.destroy()

class editProducts():
    def __init__(self,previousWin):
        #Window Configuration
        self.win = tk.Toplevel(previousWin)
        self.win.title("Edit Products")
        self.win.geometry("500x300")
        self.win.rowconfigure(0,weight=1)
        self.win.columnconfigure(1,weight=1)
        
        #Frame Configuration
        editProductsFrame = tk.Frame(master=self.win)
        editProductsFrame.grid(row=0,column=1, sticky="nsew")
        
        #Label Configuration
        nameLabel = tk.Label(master=editProductsFrame, text="Product Name:")
        nameLabel.place(x=115,y=60, width=100,height=20)
        
        #Button Configuration
        exitButton = tk.Button(master= editProductsFrame,text="Exit")
        exitButton['command'] = self.win.destroy
        exitButton.place(x=5,y=5,width=100, height=50)
        
        submitButton = tk.Button(master= editProductsFrame, text="Submit")
        submitButton['command'] = self.findInDB
        submitButton.place(x=395,y=245,width=100,height=50)
        
        #Textbox Configuration
        self.nameText = tk.Text(master=editProductsFrame)
        self.nameText.place(x=230,y=60,width=200,height=20)
        
    def findInDB(self):
        name = self.nameText.get("1.0", "end").strip()
        
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM item WHERE itemName = '{0}'".format(name))
        items = cur.fetchall()
        print("Results")
        for item in items:
            print(item)
        conn.close()
        if len(items) == 0:
            showinfo("Warning", "There isn't any items with this name!")
        else:
            SelectItem(self.win,items,"edit")

class SelectItem():
    def __init__(self, previousWindow, possibleItems, functions):
        #Window Configuration
        self.items = possibleItems
        self.function = functions
        self.currentItem = 0
        self.win = tk.Toplevel(previousWindow)
        self.win.title("Select a Item")
        self.win.geometry("500x300")
        self.win.rowconfigure(0, weight=1)
        self.win.columnconfigure(1, weight=1)

        #Frame Configuration
        selectItemFrame = tk.Frame(master=self.win)
        selectItemFrame.grid(row=0, column=1, sticky="nsew")

        #Button Configuration
        exitButton = tk.Button(master=selectItemFrame, text="Exit")
        exitButton['command'] = self.win.destroy
        exitButton.place(x=5,y=5,width=100,height=50)
        
        selectButton = tk.Button(master=selectItemFrame, text="Submit")
        selectButton['command'] = self.submit
        selectButton.place(x=200, y=245,width=100, height=50)
        
        nextButton = tk.Button(master=selectItemFrame, text="Next")
        nextButton['command'] = self.nextItem
        nextButton.place(x=395, y=175, width=100,height=50)
        
        previousButton = tk.Button(master=selectItemFrame, text="Previous")
        previousButton['command'] = self.previousItem
        previousButton.place(x=5, y=175, width=100, height=50)
        
        #Label Configuration
        nameLabel = tk.Label(master=selectItemFrame, text="Item Name:")
        nameLabel.place(x=115,y=60, width=100,height=20)
        
        priceLabel = tk.Label(master=selectItemFrame, text="Item Price:")
        priceLabel.place(x=115,y=90, width=100, height=20)
        
        qantityLabel = tk.Label(master=selectItemFrame, text="Quantity:")
        qantityLabel.place(x=115, y=120,width=100, height=20)
        
        #Textbox Configuration
        self.nameText = tk.Text(master=selectItemFrame)
        self.nameText.place(x=230,y=60,width=200,height=20)
        
        self.priceText = tk.Text(master=selectItemFrame)
        self.priceText.place(x=230,y=90,width=200,height=20)
        
        self.quantityText = tk.Text(master=selectItemFrame)
        self.quantityText.place(x=230,y=120,width=200,height=20)

        self.firstItem()
        

    def firstItem(self):
        firstItem = self.items[0]
        print("First Item: {0}".format(firstItem))
        self.nameText.insert("1.0", firstItem[2])
        self.priceText.insert("1.0", firstItem[3])
        self.quantityText.insert("1.0", firstItem[4])

    def nextItem(self):
        #This function will load the next item in the list
        #If it reaches the end of the list it will loop back around to the first item.
        
        #Makes the Textboxes Blank
        self.nameText.delete("1.0",'end')
        self.priceText.delete("1.0",'end')
        self.quantityText.delete("1.0",'end')
        
        # print(len(self.profiles))
        self.currentItem = self.currentItem + 1
        
        #Checks if self.currentItem goes over the number of items found and if it is sets it back to 0
        if (self.currentItem + 1) > len(self.items):
            self.currentItem = 0
        profile = self.items[self.currentItem]
        
        #Updates textboxes
        self.nameText.insert("1.0", profile[2])
        self.priceText.insert("1.0", profile[3])
        self.quantityText.insert("1.0", profile[4])

    def previousItem(self):
        #This functions will the load the previous profile in the list
        #If it is the first item in the list it will loop to the last profile in the list
        
        #Makes the Textboxes Blank
        self.nameText.delete("1.0",'end')
        self.priceText.delete("1.0",'end')
        self.quantityText.delete("1.0",'end')
        
        # print(len(self.profiles))
        self.currentItem = self.currentItem - 1
        #Checks if self.currentProfile is below 0 if it is it will set it to the max of the list
        if(self.currentItem) < 0:
            self.currentItem = (len(self.items)-1)
        #Grabs profile from list
        profile = self.items[self.currentItem]
        #Updates textboxes
        self.nameText.insert("1.0", profile[2])
        self.priceText.insert("1.0", profile[3])
        self.quantityText.insert("1.0", profile[4])
    
    def submit(self):
        #Goto changes values to make the changes to that item.
        print(self.items[self.currentItem])
        if self.function == "edit":
            editItem(self.win, self.items[self.currentItem])
            print()
        elif self.function == "delete":
            deleteItem(self.win,self.items[self.currentItem])
        else:
            showinfo("Error", "Error: class: SelectProfile, Function:submit, self.function is not 'edit' or 'delete'")

class editItem():
    def __init__(self,previousWin, currentItems):
        #Window Configuration
        self.item = currentItems
        self.win = tk.Toplevel(previousWin)
        self.win.title("Edit the Item")
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
        submitButton.place(x=395,y=245,width=100,height=50)
        
        #Label Configuration
        nameLabel = tk.Label(master=editCustomerFrame, text="First Name:")
        nameLabel.place(x=115,y=60, width=100,height=20)
        
        priceLabel = tk.Label(master=editCustomerFrame, text="Last Name:")
        priceLabel.place(x=115,y=90, width=100, height=20)
        
        quantityLabel = tk.Label(master=editCustomerFrame, text="Contact Number:")
        quantityLabel.place(x=91, y=120,width=110, height=20)
        
        instructionLabel = tk.Label(master=editCustomerFrame,text="Edit This Item then press \nSubmit to commit changes!")
        instructionLabel.place(x=105,y=5, width=300,height=40)
        
        #Textbox Configuration
        self.nameText = tk.Text(master=editCustomerFrame)
        self.nameText.place(x=230,y=60,width=200,height=20)
        
        self.priceText = tk.Text(master=editCustomerFrame)
        self.priceText.place(x=230,y=90,width=200,height=20)
        
        self.quantityText = tk.Text(master=editCustomerFrame)
        self.quantityText.place(x=230,y=120,width=200,height=20)

        self.loadDataFromDB()


    def loadDataFromDB(self):
        name = self.item[2]
        price = self.item[3]
        quantity = self.item[4]
        
        self.nameText.insert("1.0", name)
        self.priceText.insert("1.0",price)
        self.quantityText.insert("1.0",quantity)

    def commitToDB(self):
        name = self.nameText.get("1.0", "end").strip()
        price = self.priceText.get("1.0", "end").strip()
        quantity = self.quantityText.get("1.0", "end").strip()
        itemID = self.item[1]
        
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        cur.execute("UPDATE item SET itemName = '{0}', itemPrice = '{1}', quantity = '{2}' WHERE ItemID = '{3}'".format(name,price,quantity,itemID))
        conn.commit()
        conn.close()
        print("Item updated:")
        print("{0}, {1}, {2}".format(name,price,quantity))
        

class DeleteProductsMenu():
    def __init__(self, previousWin):
        #Window Configuration
        self.win = tk.Toplevel(previousWin)
        self.win.title("Delete a Customer")
        self.win.geometry("500x300")
        self.win.rowconfigure(0, weight=1)
        self.win.columnconfigure(1, weight=1)
        
        #Frame Configure
        deleteProductFrame = tk.Frame(master=self.win)
        deleteProductFrame.grid(row=0 ,column=1, sticky="nsew")
        
        #Label Configuration
        nameLabel = tk.Label(master=deleteProductFrame, text="Item Name:")
        nameLabel.place(x=115, y=60, width=100, height=20)
        
        #Button Configuration
        exitButton = tk.Button(master=deleteProductFrame, text="Exit")
        exitButton['command'] = self.win.destroy
        exitButton.place(x=5,y=5, width=100,height=50)
        
        searchButton = tk.Button(master=deleteProductFrame, text="Search")
        searchButton['command'] = self.findDataDB
        searchButton.place(x=200,y=240, width=100,height=50)
        
        #Textbox Configuration
        self.nameText = tk.Text(master=deleteProductFrame)
        self.nameText.place(x=230, y=60, width=200,height=20)
    
    def findDataDB(self):
        name = self.nameText.get("1.0", "end").strip()

        
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM item WHERE itemName = '{0}'".format(name))
        items = cur.fetchall()
        print("Results:")
        for item in items:
            print(item)
        conn.close()
        if len(items) == 0:
            showinfo(title="Warning", message="There isn't any items with these details!")
        else:
            SelectItem(self.win, items, "delete")

class deleteItem():
    def __init__(self, previousWin, item):
        #Window Configuration
        self.item = item
        self.win = tk.Toplevel(previousWin)
        self.win.title("Delete This Profile?")
        self.win.geometry("500x300")
        self.win.rowconfigure(0, weight=1)
        self.win.columnconfigure(1, weight=1)
        
        #Frame Configuration
        deleteProfileFrame = tk.Frame(master = self.win)
        deleteProfileFrame.grid(row=0, column=1, sticky="nsew")
        
        #Label Configuration
        nameLabel = tk.Label(master=deleteProfileFrame, text="Item Name")
        nameLabel.place(x=115,y=60, width=100,height=20)
        
        priceLabel = tk.Label(master=deleteProfileFrame, text="Item Price")
        priceLabel.place(x=115,y=90, width=100, height=20)
        
        quantityLabel = tk.Label(master=deleteProfileFrame, text="Quantity")
        quantityLabel.place(x=91, y=120,width=110, height=20)
                
        #Button Configuration
        exitButton = tk.Button(master= deleteProfileFrame,text="Exit")
        exitButton['command'] =self.win.destroy
        exitButton.place(x=5,y=5,width=100, height=50)
        
        submitButton = tk.Button(master= deleteProfileFrame, text="Delete")
        submitButton['command'] = self.deleteProfile
        submitButton.place(x=395,y=245,width=100,height=50)
        
        #Textbox Configuration
        self.nameText = tk.Text(master=deleteProfileFrame)
        self.nameText.place(x=230,y=60,width=200,height=20)
        
        self.priceText = tk.Text(master=deleteProfileFrame)
        self.priceText.place(x=230,y=90,width=200,height=20)
        
        self.quantityText = tk.Text(master=deleteProfileFrame)
        self.quantityText.place(x=230,y=120,width=200,height=20)
        
        
        self.loadProfile()
        
    def loadProfile(self):
        name = self.item[2]
        price = self.item[3]
        quantity = self.item[4]
        
        self.nameText.insert("1.0", name)
        self.priceText.insert("1.0",price)
        self.quantityText.insert("1.0",quantity)
        
    def deleteProfile(self):
        print("Deleting Profile: {0}".format(self.item))
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM item WHERE itemID = '{0}'".format(self.item[1]))
        conn.commit()
        conn.close()

