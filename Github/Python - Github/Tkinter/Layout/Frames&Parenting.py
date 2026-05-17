import tkinter as tk 
from tkinter import ttk

#window 
window=tk.Tk()
window.title('Frames & Parenting ')
window.geometry('600x400')

#frame 
frame=ttk.Frame(
    master=window,
    width=200,
    height=200,
    borderwidth=10,
      )# defult is relief=ttk.FLAT or RAISED OR SUNKEN or GROOVE or RIDGE 
frame.pack_propagate(False) #so that the height and width don't change depending on the widget inside 
frame.pack(side='left')

# parrenting or "Master Setting"
label=ttk.Label(master=frame,text='label in frame',)
label.pack()

button= ttk.Button(master=frame, text='A button in a frame')
button.pack()

#example
label2=ttk.Label(master=window, text='A label in window')
label2.pack(side='left')

#run 
window.mainloop()