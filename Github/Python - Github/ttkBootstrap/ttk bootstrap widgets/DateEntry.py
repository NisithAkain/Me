import tkinter as tk 
import ttkbootstrap as ttk 
from ttkbootstrap.widgets import DateEntry

#window
window = ttk.Window()
window.title('toast ')

#calender
calendar = DateEntry(window)
calendar.pack(pady=10)

ttk.Button(window, text ='get calendar', command = lambda:print(calendar.entry.get())).pack() #. entry the entry widget in the calander (TARGETED)

#run 
window.mainloop()