from   tkinter import *
from openpyxl.workbook import Workbook
from   tkinter import messagebox as msg
import sys
import pandas as pd
import os.path
import csv
from tkintertable import TableCanvas 
class create_exls:

     def __init__(self, root):
          self.f = Frame(root, height=350, width=500)
          self.f.pack()    # Place the frame on root window
           
          # Creating label widgets
          self.message_label = Label(self.f,text='Convert  CSV file to exls file',font=('Arial', 14))
          
          # Buttons
          self.confirm_button = Button(self.f,text='Display', font=('Arial', 14), bg='Orange',
                                 fg='Black', command=self.conv_to_exls)
          self.exit_button = Button(self.f,text='Exit', font=('Arial', 14), bg='Yellow',
                                 fg='Black', command=root.destroy)

          # Placing the widgets using grid manager
          self.message_label.grid(row=1, column=0)
          self.confirm_button.grid(row=2,column=0)
          self.exit_button.grid(row=2,column=2)
     def conv_to_exls(self):
         df=pd.read_csv('empsal.csv')
         df.to_excel("empsal.xlsx",index=None,header=True)
root=Tk()
root.title('Build/Display CSV in Tkintertable')
root.geometry('1000x600')
conv_csv = create_exls(root)
root.mainloop()
