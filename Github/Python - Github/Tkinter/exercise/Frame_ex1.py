import tkinter as tk 
import ttkbootstrap as ttk
import time as tm

def App_command():
    x=entry.get()
    label['text']=x

def return_back():
    label['text']='A button in frame'
    
    
#widnow
window=ttk.Window(themename='darkly')
window.title('Excersise 1 ')
window.geometry('600x400')

#frame
frame=ttk.Frame(master=window,width=200,height=200,borderwidth=10, relief=ttk.GROOVE)
frame.pack_propagate(False)
frame.pack(side='right')

#widgets in frame 
label=ttk.Label(master=frame, text='A label in frame')
label.pack()

button=ttk.Button(master=frame,text='A button in frame', command=App_command)
button.pack()

entry=ttk.Entry(master=frame)
entry.pack()

button2 =ttk.Button(master=frame, text='return', command=return_back)
button2.pack()
#run 
window.mainloop()