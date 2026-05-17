import tkinter as tk
import ttkbootstrap as ttk 
from ttkbootstrap.widgets import Meter

#window
window = ttk.Window()
window.title('toast ')

#meter
meter = ttk.Meter(window, 
                  amounttotal=100,
                  amountused=0,
                  interactive=True,
                  metertype = 'semi',
                  subtext = "some other text",
                  bootstyle='danger')
                
meter.pack()

#run 
window.mainloop()
