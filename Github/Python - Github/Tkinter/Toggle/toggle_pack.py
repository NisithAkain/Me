import tkinter as tk
from tkinter import ttk

# setup
window= tk.Tk()
window.geometry('600x400')
window.title('Hide Widgets')

#place


def toggle_label_place():
    global label_visible

    if label_visible == True:
        label.pack_forget()
        label_visible=False
    else:
        label_visible=True
        label.pack(side='left',expand= True, before= button)


button = ttk.Button(master= window, text = "toggle Label", command = toggle_label_place )
button.pack(side='right')

label_visible = True
label= ttk.Label(master = window, text = 'A label')
label.pack(side='left')

#run 
window.mainloop()