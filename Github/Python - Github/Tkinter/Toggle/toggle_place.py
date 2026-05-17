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
        label.place_forget()
        label_visible=False
    else:
        label_visible=True
        label.place(relx = 0.5, rely =0.5, anchor = 'center' )


button = ttk.Button(master= window, text = "toggle Label", command = toggle_label_place )
button.place(x=10, y=10)

label_visible = True
label= ttk.Label(master = window, text = 'A label')
label.place(relx = 0.5, rely =0.5, anchor = 'center' )

#run 
window.mainloop()