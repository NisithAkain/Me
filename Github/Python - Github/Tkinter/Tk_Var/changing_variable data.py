import tkinter as tk 
import ttkbootstrap as ttk

def button_func():
    print(entry.get()) # eaiest way to get information in a widget 
    # update the label
    Output = entry.get()
    label['text']= Output # or label.config(text= Output)
    entry['state']='disabled' #means widget is no longer useable 

def return_func():
    entry['state']='anabled'
    label['text']='some text'


#window
window=ttk.Window(themename ='darkly')
window.title("getting data ")

# windgets
label=ttk.Label(master=window,text="some text")
label.pack()

#TTK frame
title_frame = ttk.Frame(master=window) # to format the enter button next to entry, makes another window to put idgets in 
title_frame.pack()


entry = ttk.Entry(master=title_frame)
entry.pack(side='left',padx=10)
button =ttk.Button(master=title_frame, text= "enter", command= button_func)
button.pack(side='left')

# excersise 
return_button = ttk.Button(master=window, text="return" ,command=return_func)
return_button.pack()
#run 
window.mainloop()