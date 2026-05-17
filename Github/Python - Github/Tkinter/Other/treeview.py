import tkinter as tk 
import ttkbootstrap as ttk 
from random import choice
#window 
window = ttk.Window(themename='darkly')
window.title('treeview')
window.geometry('600x500')

#data 
first_names = ['bob','jeromy','tom','benjiman','sam','paul','jack','caleb','sonny','ben','jeromy','steven']
last_names =['jefferson','margarita','adiotana','he','chifa','haselo','bayfish','fishbait','sharktail']

#treeview
table =ttk.Treeview(master=window, columns=('first','last','email'), show='headings')
table.heading('first',text='first name')
table.heading('last',text='Surname')
table.heading('email', text ='email')
table.pack(fill='both',expand=True)

#insert values into table 
table.insert(parent='',index=0,values =('bob','jefferson','bobjefferson@gmail.com'))
for i in range(100):
    first=choice(first_names)
    last =choice(last_names)
    email =f'{first}{last}@gmail.com'
    data =(first,last,email)
    table.insert(parent='',index=0,values=data)

table.bind('<<TreeviewSelect>>',lambda event: print(table.selection()))
#run 
window.mainloop()
