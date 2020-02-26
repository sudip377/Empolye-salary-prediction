from   tkinter import *
from   tkinter import messagebox as msg
import pandas as pd

from pandastable import Table
class Dis_sum_mean_std_gen:

     def __init__(self, root):
          self.f = Frame(root, height=350, width=500)
          self.f.pack()    # Place the frame on root window
           
          # Creating label widgets
          self.message_label = Label(self.f,text='DISPLAY SUM MEAN STANDARD DEVIATION',fg='blue',font=('Arial', 14))
          
          # Buttons
          self.confirm_button = Button(self.f,text='CLICK HERE FOR SALARY', font=('Arial', 10), bg='Orange',
                                 fg='Black', command=self.sum_mean_std_gen_SALARY)
          self.confirm_button1 = Button(self.f,text='CLICK HERE FOR HRA', font=('Arial', 10), bg='Orange',
                                 fg='Black', command=self.sum_mean_std_gen_HRA)
          self.confirm_button2 = Button(self.f,text='CLICK HERE FOR CONV', font=('Arial', 10), bg='Orange',
                                 fg='Black', command=self.sum_mean_std_gen_CONV)


          self.exit_button = Button(self.f,text='Exit', font=('Arial', 10), bg='red',
                                 fg='Black', command=root.destroy)

          # Placing the widgets using grid manager
          self.message_label.grid(row=1, column=0)
          self.confirm_button.grid(row=2,column=0)
          self.confirm_button1.grid(row=2,column=1)
          self.confirm_button2.grid(row=2,column=2)
          self.exit_button.grid(row=2,column=3)
     def sum_mean_std_gen_SALARY(self):
         df=pd.read_csv('empsal.csv')
         salarym=df.loc[df['sex']=='M','salary'].sum()
         salaryf=df.loc[df['sex']=='F','salary'].sum()
         salaryme=df.loc[df['sex']=='M','salary'].mean()
         salarymf=df.loc[df['sex']=='F','salary'].mean()
         salarystd=df.loc[df['sex']=='M','salary'].std()
         salarystf=df.loc[df['sex']=='F','salary'].std()
         
         df1=pd.DataFrame([salarym,salaryf])
         df1['mean'] = pd.Series([salaryme,salarymf])
         df1['std'] = pd.Series([salarystd,salarystf])
         df1.index = ['Male','Female']
         df1.columns = ['Sum','Mean','Standard Dev']
         self.f = Frame(root, height=200, width=300) 
         self.f.pack(fill=BOTH,expand=1)
         self.table = Table(self.f, dataframe=df1,read_only=True)
         self.table.show()
     def sum_mean_std_gen_HRA(self):
         df=pd.read_csv('empsal.csv')
         hra_m=df.loc[df['sex']=='M','hra'].sum()
         hra_f=df.loc[df['sex']=='F','hra'].sum()
         hra_me=df.loc[df['sex']=='M','hra'].mean()
         hra_mf=df.loc[df['sex']=='F','hra'].mean()
         hra_std=df.loc[df['sex']=='M','hra'].std()
         hra_stf=df.loc[df['sex']=='F','hra'].std()
         
         df1=pd.DataFrame([hra_m,hra_f])
         df1['mean'] = pd.Series([hra_me,hra_mf])
         df1['std'] = pd.Series([hra_std,hra_stf])
         df1.index = ['Male','Female']
         df1.columns = ['Sum','Mean','Standard Dev']
         self.f = Frame(root, height=200, width=300) 
         self.f.pack(fill=BOTH,expand=1)
         self.table = Table(self.f, dataframe=df1,read_only=True)
         self.table.show()
     def sum_mean_std_gen_CONV(self):
         df=pd.read_csv('empsal.csv')
         conv=(df['salary']*10)//100
         df['conv']=df['salary']*0.1
         conv_m=df.loc[df['sex']=='M','conv'].sum()
         conv_f=df.loc[df['sex']=='F','conv'].sum()
         conv_me=df.loc[df['sex']=='M','conv'].mean()
         conv_mf=df.loc[df['sex']=='F','conv'].mean()
         conv_std=df.loc[df['sex']=='M','conv'].std()
         conv_stf=df.loc[df['sex']=='F','conv'].std()
         
         df1=pd.DataFrame([conv_m,conv_f])
         df1['mean'] = pd.Series([conv_me,conv_mf])
         df1['std'] = pd.Series([conv_std,conv_stf])
         df1.index = ['Male','Female']
         df1.columns = ['Sum','Mean','Standard Dev']
         self.f = Frame(root, height=200, width=300) 
         self.f.pack(fill=BOTH,expand=1)
         self.table = Table(self.f, dataframe=df1,read_only=True)
         self.table.show()
#--------------------------------------------------
root=Tk()
root.title('Build/Display CSV in Tkintertable')
root.geometry('1000x900')
conv_df = Dis_sum_mean_std_gen(root)
root.configure(bg='yellow')
root.mainloop()

