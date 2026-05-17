import tkinter as tk 
from tkinter import ttk 

def create_segment(parent, label_text, button_text):
    frame = ttk.Frame(master = parent)
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure((0,1,2), weight=1, uniform = 'a')

    #widgets 
    ttk.Label(frame, text =label_text).grid(row=0, column=0, sticky ='nsew')
    ttk.Button(frame, text=button_text).grid(row=0, column=1, sticky = 'nsew')

    frame.pack(expand=True, fill = 'both')
   
    return frame

#window
window = tk.Tk()
window.title('widgets and return ')
window.geometry('400x600')


#widgets 
create_segment(window, 'label', 'button').pack(expand = True, fill ='both')
create_segment(window, 'test', 'click').pack(expand = True, fill ='both')
create_segment(window, 'hello', 'test').pack(expand = True, fill ='both')
create_segment(window, 'bye', 'launch').pack(expand = True, fill ='both')
create_segment(window, 'last one', 'exit').pack(expand = True, fill ='both')

#run 
window.mainloop()