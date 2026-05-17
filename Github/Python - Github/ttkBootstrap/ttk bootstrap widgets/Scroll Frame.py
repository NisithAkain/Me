import tkinter as tk 
import ttkbootstrap as ttk 
from ttkbootstrap.scrolled import ScrolledFrame

#window
window = ttk.Window()
window.title('scroll frame ')

#scroll frame
scroll_frame = ScrolledFrame(window)
scroll_frame.pack(expand = True, fill = 'both')

for i in range(100):
    ttk.Label(scroll_frame, text = f'Label: {i}').pack(fill ='x') 
    ttk.Button(scroll_frame,text = f'Button: {i}').pack(fill='x')
#very laggy and limited

#run 
window.mainloop()