import sqlite3
import tkinter as tk
from tkinter.messagebox import showinfo
import os

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
        deleteCustomer['command'] = self.deleteCustomer
        deleteCustomer.place(x=90,y=200,width=125,height=50)
    def addCustomer(self):
        addCustomers(self.win)
    def editCustomer(self):
        editCustomers(self.win)
    def deleteCustomer(self):
        deleteCustomers(self.win)

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
        self.win.destroy()

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
            SelectProfile(self.win, profiles, "edit")

class SelectProfile():
    def __init__(self,previousWindow, possibleProfiles, function):
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
        else:
            showinfo("Error", "Error: class: SelectProfile, Function:submit, self.function is not 'edit' or 'delete'")
    # def __class_getitem__(self):
    #     return self.profiles[self.currentProfile]   
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
        submitButton.place(x=395,y=245,width=100,height=50)
        
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
        
class deleteCustomers():
    def __init__(self, previousWin):
        #Window Configuration
        self.win = tk.Toplevel(previousWin)
        self.win.title("Delete a Customer")
        self.win.geometry("500x300")
        self.win.rowconfigure(0, weight=1)
        self.win.columnconfigure(1, weight=1)
        
        #Frame Configure
        deleteCustomerFrame = tk.Frame(master=self.win)
        deleteCustomerFrame.grid(row=0 ,column=1, sticky="nsew")
        
        #Label Configuration
        fNameLabel = tk.Label(master=deleteCustomerFrame, text="First Name:")
        fNameLabel.place(x=115, y=60, width=100, height=20)
        
        lNameLabel = tk.Label(master=deleteCustomerFrame, text="Last Name:")
        lNameLabel.place(x=115, y=90, width=100, height=20)
        
        #Button Configuration
        exitButton = tk.Button(master=deleteCustomerFrame, text="Exit")
        exitButton['command'] = self.win.destroy
        exitButton.place(x=5,y=5, width=100,height=50)
        
        searchButton = tk.Button(master=deleteCustomerFrame, text="Search")
        searchButton['command'] = self.findDataDB
        searchButton.place(x=200,y=240, width=100,height=50)
        
        #Textbox Configuration
        self.fNameText = tk.Text(master=deleteCustomerFrame)
        self.fNameText.place(x=230, y=60, width=200,height=20)
        
        self.lNameText = tk.Text(master= deleteCustomerFrame)
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
            SelectProfile(self.win, profiles, "delete")
                
class deleteProfile():
    def __init__(self, previousWin, profile):
        #Window Configuration
        self.profile = profile
        self.win = tk.Toplevel(previousWin)
        self.win.title("Delete This Profile?")
        self.win.geometry("500x300")
        self.win.rowconfigure(0, weight=1)
        self.win.columnconfigure(1, weight=1)
        
        #Frame Configuration
        deleteProfileFrame = tk.Frame(master = self.win)
        deleteProfileFrame.grid(row=0, column=1, sticky="nsew")
        
        #Label Configuration
        fNameLabel = tk.Label(master=deleteProfileFrame, text="First Name:")
        fNameLabel.place(x=115,y=60, width=100,height=20)
        
        lNameLabel = tk.Label(master=deleteProfileFrame, text="Last Name:")
        lNameLabel.place(x=115,y=90, width=100, height=20)
        
        contactLabel = tk.Label(master=deleteProfileFrame, text="Contact Number:")
        contactLabel.place(x=91, y=120,width=110, height=20)
        
        addressLabel = tk.Label(master=deleteProfileFrame, text="Address:")
        addressLabel.place(x=120, y=150, width=100,height=20)
        
        #Button Configuration
        exitButton = tk.Button(master= deleteProfileFrame,text="Exit")
        exitButton['command'] =self.win.destroy
        exitButton.place(x=5,y=5,width=100, height=50)
        
        submitButton = tk.Button(master= deleteProfileFrame, text="Delete")
        submitButton['command'] = self.deleteProfile
        submitButton.place(x=395,y=245,width=100,height=50)
        
        #Textbox Configuration
        self.fNameText = tk.Text(master=deleteProfileFrame)
        self.fNameText.place(x=230,y=60,width=200,height=20)
        
        self.lNameText = tk.Text(master=deleteProfileFrame)
        self.lNameText.place(x=230,y=90,width=200,height=20)
        
        self.contactText = tk.Text(master=deleteProfileFrame)
        self.contactText.place(x=230,y=120,width=200,height=20)
        
        self.addressText = tk.Text(master=deleteProfileFrame)
        self.addressText.place(x=230,y=150,width=200,height=20)
        
        self.loadProfile()
        
    def loadProfile(self):
        fName = self.profile[2]
        lName = self.profile[3]
        address = self.profile[4]
        contact = self.profile[5]
        
        self.fNameText.insert("1.0", fName)
        self.lNameText.insert("1.0",lName)
        self.addressText.insert("1.0",address)
        self.contactText.insert("1.0",contact)
        
    def deleteProfile(self):
        print("Deleting Profile: {0}".format(self.profile))
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM customer WHERE CusID = '{0}'".format(self.profile[1]))
        conn.commit()
        conn.close()        
        