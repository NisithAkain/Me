import tkinter as tk 
import ttkbootstrap as ttk 
from ttkbootstrap.tooltip import ToolTip

#window
window = ttk.Window()
window.title('tooltip')


#tooltip, small hover message 
button = ttk.Button(window, text='button', bootstyle='warning')
button.pack()
ToolTip(button, text='this does something', bootstyle='danger')

#run 
window.mainloop()