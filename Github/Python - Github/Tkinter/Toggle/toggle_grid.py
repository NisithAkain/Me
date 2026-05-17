import tkinter as tk
from tkinter import ttk

#window
window =tk.Tk()
window.title('toggle widgets')
window.geometry('500x600')


def toggle():
    global label_visible

    if label_visible == True:
        Label.grid_forget()
        label_visible=False
    else:
        Label.grid(row = 3, column=3)
        label_visible=True


#row/column
window.rowconfigure(1,weight=1)
window.rowconfigure(2,weight=1)
window.rowconfigure(3,weight=1)
window.rowconfigure(4,weight=1)

window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=1)
window.columnconfigure(3,weight=1)
window.columnconfigure(4,weight=1)


#widgets 
checkbutton_var = tk.IntVar(value=1)
checkbutton = ttk.Checkbutton(master = window, text = 'toggle',variable=checkbutton_var, command =toggle)
checkbutton.grid(row= 1, column=1)


label_visible = True
Label = ttk.Label(master = window,text ='label')
Label.grid(row = 3, column=3)

#run 
window.mainloop()
