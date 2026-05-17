import tkinter as tk 
from tkinter import ttk 

# window
window = tk.Tk()
window.geometry('600x400')
window.title('layout intro')

# widgets 
label1 = ttk.Label(master=window, text = 'label 1 ', background='red')
label2 = ttk.Label(master=window, text = 'label 2 ', background='blue')


#grid
window.columnconfigure(0, weight = 1 ) # //(specific number, weight = width )
window.columnconfigure(1, weight = 1 )
window.columnconfigure(2, weight = 2 )
window.rowconfigure(0, weight =1 ) # //( specific number, weight = height )

label1.grid(row = 0, column = 1, sticky = 'nsew')# where widget lays -sticky = n, s , e, w ..ect
label2.grid(row=0, column = 0,columnspan = 1,  sticky ='nsew') # columnspan how many rows it occupies from grid 


#run 
window.mainloop()