

from   tkinter import *
from   tkinter import messagebox as msg
import pandas as pd

from pandastable import Table

class create_df:

     def __init__(self, root):
          self.f = Frame(root, height=350, width=500)
          self.f.pack()    
           
          
          self.message_label = Label(self.f,text='Convert "CSV FILE"  to Pandas "DF"',font=('Arial', 14))
          
          
          self.confirm_button = Button(self.f,text='Convert', font=('Arial', 14), bg='Orange',
                                 fg='Black', command=self.conv_to_df)
          self.exit_button = Button(self.f,text='Exit', font=('Arial', 14), bg='red',
                                 fg='Black', command=root.destroy)

          
          self.message_label.grid(row=1, column=0)
          self.confirm_button.grid(row=2,column=0)
          self.exit_button.grid(row=2,column=2)
     
     def conv_to_df(self):
             empsal_df = pd.read_csv("empsal.csv")
             #empsal_df.set_index('empno',inplace=True)
             self.f = Frame(root, height=200, width=300) 
             self.f.pack(fill=BOTH,expand=1)
             self.table = Table(self.f, dataframe=empsal_df,read_only=True)
             self.table.show()

     def add_col(self):
             df=pd.read_csv('empsal.csv')
             df['conv']=(df.salary*10)//100
             df['total']=df.salary+df.hra+df.conv
             self.f = Frame(root, height=200, width=300) 
             self.f.pack(fill=BOTH,expand=1)
             self.table = Table(self.f, dataframe=df,read_only=True)
             self.table.show()
      

root=Tk()
root.title('Convert "CSV FILE"  to Pandas "DF"')
root.geometry('800x600')
root.configure(bg='yellow')
conv_csv = create_df(root)
root.mainloop()

