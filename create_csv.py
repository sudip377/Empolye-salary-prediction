from   tkinter import *
from   tkinter import messagebox as msg
import sys
import pandas as pd
import os.path
import csv
from tkintertable import TableCanvas 
class create_csv:

     def __init__(self, root):
          self.f = Frame(root, height=350, width=500)
          self.f.pack()    # Place the frame on root window
           
          # Creating label widgets
          self.message_label = Label(self.f,text='Display the Empsal.CSV in TkinterTable',font=('Arial', 14))
          
          # Buttons
          self.confirm_button = Button(self.f,text='Display', font=('Arial', 14), bg='Orange',
                                 fg='Black', command=self.conv_to_csv)
          self.exit_button = Button(self.f,text='Exit', font=('Arial', 14), bg='red',
                                 fg='Black', command=root.destroy)

          # Placing the widgets using grid manager
          self.message_label.grid(row=1, column=0)
          self.confirm_button.grid(row=2,column=0)
          self.exit_button.grid(row=2,column=2)
     def conv_to_csv(self):
         
         try:
                     
             # Now display the CSV in 'tkintertable' widget
             self.f = Frame(root, height=200, width=300) 
             self.f.pack(fill=BOTH,expand=1)
             self.table = TableCanvas(self.f, read_only=True)
             self.table.importCSV('empsal.csv')
             self.table.show()
        
         except FileNotFoundError as e:
             msg.showerror('Error in opening file', e.msg)
          
#--------------------------------------------------
root=Tk()
root.title('Build/Display CSV in Tkintertable')
root.geometry('1000x600')
conv_csv = create_csv(root)
#root.configure(bg='orange')
root.mainloop()
