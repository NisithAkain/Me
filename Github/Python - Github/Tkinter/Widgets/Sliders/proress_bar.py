import tkinter as tk
import ttkbootstrap as ttk

#window
window=ttk.Window(themename='darkly')
window.title('Progress Bar')

#slider
slider_float=ttk.IntVar(value=15)
scale=ttk.Scale(
    master=window,
    length=300,
    orient='vertical',
    variable=slider_float,
    from_=0,
    to=20)
scale.pack()
#progress bar
progress=ttk.Progressbar(
    master=window,
    variable=slider_float,
    maximum=20,
    orient='horizontal',
    mode='determinate',
    length=400) # determinate,progressive or indeterminate,not progressivebar
progress.pack()
#label
label=ttk.Label(master=window,textvariable=slider_float)
label.pack()
#run 
window.mainloop()