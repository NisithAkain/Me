import tkinter as tk
import ttkbootstrap as ttk

#window 
window=ttk.Window(themename='journal')
window.geometry('600x400')
window.title("Akain project 1 ")

# Menu 
Menu=ttk.Menu(master=window)

# sub menu
sub_menu1=ttk.Menu(master=Menu, tearoff= False )
Menu.add_cascade(label='random menu 1 ', menu=sub_menu1)
window.configure(menu=Menu)
tabs=Menu.add


# mainloop
window.mainloop()