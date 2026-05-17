import tkinter as tk 
import ttkbootstrap as ttk

#window
window=ttk.Window(themename='journal')
window.title('Slider')

#sider
scale_float=ttk.DoubleVar(value=12.5)
scale =ttk.Scale(
    master=window,
    command=lambda value:print(scale_float.get())
    ,from_=0,to=20
    ,orient='horizontal',
    length=300,
    variable=scale_float)
scale.pack()
#run
window.mainloop()