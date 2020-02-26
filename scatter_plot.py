from   tkinter import *
from   tkinter import messagebox as msg
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
df = pd.read_csv('empsal.csv')
expyr = df['expyr']
salary = df['salary']
plt.scatter(expyr, salary, color = 'red', label='Salary')
plt.title('Salary vs Experience\nScatter Plot')
plt.xlabel('Years of Experience-->')
plt.ylabel('Salary-->')
plt.show()
#x = input('Press Enter to continue')
