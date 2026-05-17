import tkinter as tk 
import ttkbootstrap as ttk 
from tkinter import scrolledtext

#window
#window=ttk.Window(themename='darkly')
window=tk.Tk()
window.title('scrolled text')

#scrolled text
scrolled_text=scrolledtext.ScrolledText(master=window,width=100,height=100)
scrolled_text.pack()

#run
window.mainloop()
