
import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(600, 200))
        self.master.title('Check Files')
        self.master.config(bg='lightgray')

        self.varBrowse_1 = StringVar()
        self.varBrowse_2 = StringVar()

        self.btnBrowse_1 = Button(self.master, text='Browse...', width=15, height=2, fg='black', bg='lightgray')
        self.btnBrowse_1.grid(row=0, column=0, padx=(15,0), pady=(40,0))

        self.btnBrowse_2 = Button(self.master, text='Browse...', width=15, height=2, fg='black', bg='lightgray')
        self.btnBrowse_2.grid(row=1, column=0, padx=(15,0), pady=(8,0))

        self.btnCheck = Button(self.master, text='Check for files...', width=15, height=3, fg='black', bg='lightgray')
        self.btnCheck.grid(row=2, column=0, padx=(15,0), pady=(8,0))

        self.btnCancel = Button(self.master, text="Close Program", width=15, height=3, command=self.cancel)
        self.btnCancel.grid(row=2, column=2, padx=(260,2), pady=(8,0))

        self.lblDisplay = Label(self.master, text='', width=56, height=2, font=("Helvetica", 12), fg='black', bg='#fff')
        self.lblDisplay.grid(row=0, column=2, padx=(30,30), pady=(40,0))

        self.lblDisplay = Label(self.master, text='', width=56, height=2, font=("Helvetica", 12), fg='black', bg='#fff')
        self.lblDisplay.grid(row=1, column=2, padx=(30,30), pady=(2,0))


    def cancel(self):
        self.master.destroy()


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
