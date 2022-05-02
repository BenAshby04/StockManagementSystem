import sqlite3
import tkinter as tk
from tkinter.messagebox import showinfo
import os

class Folder():
    def __init__(self, previousWin):
        #Window Configuration
        self.win = tk.Toplevel(previousWin)
        self.win.title("Manage Folders")
        self.win.geometry("300x300")
        self.win.rowconfigure(0, weight=1)
        self.win.columnconfigure(1, weight=1)
        
        #Frame Configuration
        self.folderFrame = tk.Frame(master=self.win)
        self.folderFrame.grid(row=0,column=1, sticky="nsew")
        
        #Button Configuration
        exitButton = tk.Button(master=self.folderFrame, text="Exit")
        exitButton['command'] = self.win.destroy
        exitButton.place(x=5,y=5, width=100, height=50)
        
        makeFolder = tk.Button(master=self.folderFrame, text="Add a Folder")
        makeFolder['command']= self.AddFolder
        makeFolder.place(x=90, y=60, width=100, height=50)
        
        editFolder = tk.Button(master=self.folderFrame, text="Edit a Folder")
        editFolder['command'] = self.editFolder
        editFolder.place(x=90, y=130, width=100, height=50)
        
        deleteFolder = tk.Button(master=self.folderFrame, text="Delete a Folder")
        deleteFolder['command'] = self.deleteFolder
        deleteFolder.place(x=90, y=200, width=100, height=50)
        
    def AddFolder(self):
        print("Add folder selected")
        addFolder(self.win)
    def editFolder(self):
        print("Edit Folder Selected")
    def deleteFolder(self):
        print("Delete Folder Selected")
    
class addFolder():
    def __init__(self,previousWin):
        #Window Configuration
        self.win = tk.Toplevel(previousWin)
        self.win.title("Add a Folder")
        self.win.geometry("500x200")
        self.win.rowconfigure(0, weight=1)
        self.win.columnconfigure(1, weight=1)
        
        #Frame Configuration
        addFolderFrame = tk.Frame(master=self.win)
        addFolderFrame.grid(row=0, column=1, sticky="nsew")
        
        #Button Configuration
        exitButton = tk.Button(master=addFolderFrame, text="Exit")
        exitButton['command'] = self.win.destroy
        exitButton.place(x=5,y=5,width=100, height=50)
        
        submitButton = tk.Button(master=addFolderFrame, text="Submit")
        submitButton['command'] = self.commitToDB
        submitButton.place(x=395, y=145, width=100, height=50)
        
        #Label Configuration
        folderNameLabel = tk.Label(master=addFolderFrame, text="Folder Name: ")
        folderNameLabel.place(x=115, y=80, width=100, height=20)
        
        #Text Configuration
        self.folderNameText = tk.Text(master=addFolderFrame)
        self.folderNameText.place(x=230, y=80,width=200,height=20)
    
    def commitToDB(self):
        folderName = self.folderNameText.get("1.0", "end").strip()
        
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO folders (FolderName) VALUES ('{0}')".format(folderName))
        conn.commit()
        conn.close()
        print("Folder Added: {0}".format(folderName))
        self.win.destroy()

class editFolder():
    def __init__(self, previousWin):
        #Window Configuration
        self.win = tk.Toplevel(previousWin)