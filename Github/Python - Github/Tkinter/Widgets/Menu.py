import tkinter as tk 
import ttkbootstrap as ttk

#window
window=ttk.Window(themename='journal')
window.title('Menu')
window.geometry('600x400')

#menu
menu=ttk.Menu(master=window)
window.configure(menu=menu)

#sub menu
file_menu=ttk.Menu(master=menu, tearoff=False)#witout is the user can open the widget seperately as a different window
file_menu.add_command(label='New', command=lambda:print('new file'))
file_menu.add_command(label='Open', command=lambda:print('open file'))
file_menu.add_separator()#to sepreate two menus
menu.add_cascade(label='file', menu= file_menu)


# another sub menu
help_menu=ttk.Menu(master=menu, tearoff=False)
help_menu.add_command(label='help', command=lambda:print('help'))
menu.add_cascade(label='Help', menu=help_menu)
help_var=ttk.StringVar(value='on')
help_menu_check =help_menu.add_checkbutton(label='check', onvalue='on',offvalue='off', variable=help_var, command=lambda:print(help_var.get()))

#menu button
#menu_button =ttk.Menubutton(master=window, text='Menu Button')
#menu_button.pack()

#button_sub_menu=ttk.Menu(menu_button, tearoff=False)
#button_sub_menu.add_command(label='entry1', command=lambda:print('entry 1 pressed'))
#button_sub_menu.add_checkbutton(label='check1')
#menu_button.configure(menu=button_sub_menu)
#run
window.mainloop()
