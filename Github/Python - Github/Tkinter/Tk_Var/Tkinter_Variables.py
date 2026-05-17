import tkinter as tk 
import ttkbootstrap as ttk

def button_func():
    print(string_var.get())
    string_var.set('button pressed')

#window 
window = ttk.Window(themename='journal')
window.title("Tkinter Variables ")

#Thinker variables
string_var = tk.StringVar(value='start value') # StringVar, IntVVar, BooleanVar

#widgets
label=ttk.Label(master=window, text='some text', textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

button = ttk.Button(master=window,text = 'button', command=button_func)
button.pack()


# excersise 
#2 entry field and 1 label connected by a StringVar
Excersise_var=tk.StringVar(value='hello')
entry_1 = ttk.Entry(master=window,textvariable=Excersise_var)
entry_2 = ttk.Entry(master=window,textvariable = Excersise_var)
Excersise_Label = ttk.Label(master=window,textvariable=Excersise_var)
entry_1.pack()
entry_2.pack()
Excersise_Label.pack()

#run 
window.mainloop()