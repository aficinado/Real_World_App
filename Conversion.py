import tkinter as tk
from tkinter import END
win = tk.Tk()
win.geometry("600x200") 
win.title("Currency Conversion") 
font1=('Times',34,'normal') 

l1 = tk.Label(win,  text='USD', width=10,font=font1 ) 
l1.grid(row=0,column=0,padx=10,pady=10) 

m1_var=tk.DoubleVar()
m1 = tk.Entry(win,width=10,bg='yellow',font=font1,textvariable=m1_var) 
m1.grid(row=0,column=1,padx=10) 

l2 = tk.Label(win,  text='INR', width=10,font=font1 )
l2.grid(row=1,column=0,padx=10,pady=10) 

f1_var=tk.DoubleVar()
f1 = tk.Entry(win,width=10,bg='yellow',font=font1,textvariable=f1_var) 
f1.grid(row=1,column=1,padx=10) 

def my_upd1(*args):  
    m1_var.set(round(f1_var.get()*0.012,2))

def my_upd2(*args): 
    f1_var.set(round(m1_var.get()*82.98,2))    

m1.bind("<FocusOut>",my_upd2) 
f1.bind("<FocusOut>",my_upd1)

m1.bind("<FocusIn>",lambda x: m1.select_range(0,tk.END))
f1.bind("<FocusIn>",lambda x: f1.select_range(0,tk.END))
win.mainloop() 