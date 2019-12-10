import sqlite3
import shutil
import os
import time
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory



class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

     
        self.master = master
        self.master.resizable(width = True, height = True)
        self.master.geometry('{}x{}'.format(425, 225))
        self.master.title("Move Text files")
        self.master.config(bg='teal')

        # Source directory
        self.btnBrowse = Button(self.master,text="Select Directory",width=18,height=2,fg='orange',command = lambda: source_dir(self))
        self.btnBrowse.grid(row=0,column=0,padx=(20,0),pady=(40,0),sticky=S+W)

        # Displays source directory file path
        self.display1 = tk.Entry(self.master, text='')
        self.display1.grid(row=0,column=1,rowspan=1,columnspan=3,padx=(20,0),pady=(35,0))

        # Destination directory
        self.btnBrowse2 = Button(self.master,text="Select Directory",width=18,height=2,fg='orange',command = lambda: dest_dir(self))
        self.btnBrowse2.grid(row=1,column=0,padx=(20,0),pady=(20,0),sticky=S+W)

        # Displays destination directory file path
        self.display2 = tk.Entry(self.master, text='')
        self.display2.grid(row=1,column=1,rowspan=1,columnspan=3,padx=(20,0),pady=(35,0))

        # Moves text files
        self.btnMove = Button(self.master,text="Transfer Files",width=12,height=2,fg='orange',command = lambda: move_file(self))
        self.btnMove.grid(row=2,column=0,padx=(20,0),pady=(20,0),sticky=S+W)

        # Non functional close button
        self.btnClose = Button(self.master, text="Close", width=10, height=2, font=("Times", 14), fg="red")
        self.btnClose.grid(row=2,column=3,padx=(20,0),pady=(20,0),sticky=S+E)

# Function creates the source directory
def source_dir(self):
    global sourceDir
    sourceDir = filedialog.askdirectory()
    print(sourceDir) # Prints path to display box 1
    self.display1.delete(0, END)
    self.display1.insert(0, sourceDir)

# Function creates the destination directory 
def dest_dir(self):
    global destDir
    destDir = filedialog.askdirectory()
    print(destDir) # Prints path to display box 2
    self.display2.delete(0, END)
    self.display2.insert(0, destDir)

# Function creates directory to store text files
def dbUpdate(file, absPath, local_time):
    conn = sqlite3.connect('drill_123.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID  INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fileName TEXT, \
            col_filePath TEXT, \
            col_time     TEXT  \
            )")
        conn.commit()
    conn.close()
    conn = sqlite3.connect('drill_123.db')
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_files(col_fileName, col_filePath, col_time) values (?,?,?)", (file, absPath, local_time))
        conn.commit()
    conn.close()

# Function arrays through source directory for text files and prints the last modification time and destination directory path
def move_file(self):
    source = sourceDir
    dest = destDir
    for file in os.listdir(source):
        if file.endswith(".txt"):
            absPath = os.path.join(source, file)
            print(absPath) 
            modification_time = os.path.getmtime(absPath)
            local_time = time.ctime(modification_time)
            print("Last modification time(Local time):", local_time) 
            newDest = shutil.move(absPath, dest)
            print("New destination path: ", newDest)
            dbUpdate(file, absPath, local_time)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
