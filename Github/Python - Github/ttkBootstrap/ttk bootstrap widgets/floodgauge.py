import tkinter as tk 
import ttkbootstrap as ttk 
from ttkbootstrap.widgets import Floodgauge

#window
window = ttk.Window()
window.title('toast ')

#progress bar --> floodgauge
progress_int = tk.IntVar()
progress = ttk.Floodgauge(window, 
                          text ='progress',
                            variable =progress_int,
                            bootstyle='danger'
                            ,mask = 'mask {}%') #change the text 

progress.pack(pady=10,fill='x')
ttk.Scale(window,from_=0,to=100,variable = progress_int ).pack()

#run 
window.mainloop()