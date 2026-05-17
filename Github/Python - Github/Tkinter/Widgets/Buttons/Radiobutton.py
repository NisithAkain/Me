import tkinter as tk 
import ttkbootstrap as ttk 

# setup 
window= ttk.Window(themename='journal')
window.title('radiobuttons')
window.geometry('600x400')

# radiobutton 
radio_var = ttk.StringVar()
radio1 = ttk.Radiobutton(master=window, text = 'radio1', value= 'A1', variable = radio_var, command = lambda:print(radio_var.get()))
radio1.pack()
radio2 = ttk.Radiobutton(master=window, text = 'radio2', value= 'A2', variable= radio_var, command = lambda: print(radio_var.get()))
radio2.pack()
#radio buttons need different values of all will have the same value
#since both have same variable they are connected 

#run
window.mainloop()
