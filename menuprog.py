# menuprog.py 
# Menu program 

from tkinter import *
import os


class Testmenu:

    # Constructor
    def __init__(self, root):

        self.main_lbl=Label(root, text='Empolye Salary Prediction', fg='blue', font=('Arial', -30, 'bold underline'))
        self.main_lbl.place(x=200, y=250)
       
        # Create menubar
        self.menubar=Menu(root)
        root.config(menu=self.menubar)            # attach the menubar to root
        # Now create Single menubar operation menu
        self.mysql_menu=Menu(root, tearoff=0)

        self.menubar.add_cascade(label='Data Conversion', menu=self.mysql_menu)
        # Now create menu items under menubar 
        self.mysql_menu.add_command(label='Build DF', command=self.create_df)
        self.mysql_menu.add_command(label='Build CSV', command=self.create_csv)
        self.mysql_menu.add_command(label='Add Column', command=self.addnew_column)

        self.mysql_menu.add_command(label='Convert to Excel', command=self.mysql_to_xls)
         
        # Now add a separator
        self.mysql_menu.add_separator()
        # Now create a Exit menu
        self.mysql_menu.add_command(label='Exit', command=root.destroy)

        # Now create Data Maintenance operation menu
        self.data_menu=Menu(root, tearoff=0)
        self.menubar.add_cascade(label='Reports', menu=self.data_menu)
        self.data_menu.add_command(label='DIS_SUM_MEAN_STD_GENDER_WISE', command=self.rep1)
        self.data_menu.add_command(label='BAR_GRAPH_STATE_MEAN_WISE', command=self.rep2)
        self.data_menu.add_command(label='BAR_GRAPH_STATE_TOTAL_WISE', command=self.rep3)
        self.data_menu.add_command(label='SCATTER_PLOT', command=self.plot)
        
        # Prediction Menu
        self.predict_menu=Menu(root, tearoff=0)
        self.menubar.add_cascade(label='Prediction', menu=self.predict_menu)
        self.predict_menu.add_command(label='Predict', command=self.predict)
         

    def create_df(self):
        os.system("python.exe create_df.py")
    def create_csv(self):
        os.system("python.exe create_csv.py")
    def addnew_column(self):
        os.system("python.exe addnew_column.py")
    def mysql_to_xls(self):
        os.system("python.exe create_excl.py")
    
    def rep1(self):
        os.system("python.exe dis_sum_mean_std_gen.py ")
    def rep2(self):    
        os.system("python.exe  bar_graph_state_mean_wise.py")
    def rep3(self):
        os.system("python.exe bar_graph_state_total_wise.py")               
    def plot(self):
        os.system("python.exe scatter_plot.py")
        
    def predict(self):
        os.system("python.exe predict_salary.py")     
#=====================================================================================================
  
root=Tk()
root.title('Your Title Here')

obj=Testmenu(root)
root.geometry('800x600')
root.configure(bg='orange')
root.mainloop()

                                 
        
        
        
        
                 
