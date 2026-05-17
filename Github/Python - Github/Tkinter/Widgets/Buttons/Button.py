import tkinter as tk 
import ttkbootstrap as ttk 


def button_func():
    print('a button has been pressed ')

#setup
window = ttk.Window(themename='journal')
window.title('Buttons')
window.geometry('600x400')

# tkinter variables
button_string = ttk.StringVar(value='a button')
# Button 
button = ttk.Button(master=window, text='a button', command = button_func, textvariable=button_string)
button.pack()

#run 
window.mainloop()