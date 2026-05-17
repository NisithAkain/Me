import tkinter as tk
from tkinter import ttk 

#window
window = tk.Tk()
window.title('grid')
window.geometry('600x400')

#widgets 
label1 = ttk.Label(master=window, text ='Label 1', background = 'red')
label2 = ttk.Label(master=window, text ='Label 2', background = 'blue')
label3 = ttk.Label(master=window, text ='Label 3', background = 'green')
label4 = ttk.Label(master=window, text ='Label 4', background = 'yellow')
button1=ttk.Button(master=window, text = 'Button 1')
button2 = ttk.Button(master=window, text = 'Button 2 ')
entry = ttk.Entry(master = window)

#define grid
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 1)
window.columnconfigure(2, weight = 1)
window.columnconfigure(3, weight = 1)
window.rowconfigure(0, weight = 1)

#place widget  
label1.grid(row = 0, column = 0,rowspan = 3,  sticky = 'nsew') # it occupies 3 rows
label2.grid(row =0, column = 1,columnspan=4, sticky = 'w')#it occupies 3 columns 

#run 
window.mainloop()