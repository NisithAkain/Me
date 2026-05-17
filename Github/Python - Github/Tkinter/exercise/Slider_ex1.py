import tkinter as tk 
import ttkbootstrap as ttk 

#window 
window=ttk.Window(themename='darkly')
window.title('Slider ex1')

#widgets 
slider_var =ttk.DoubleVar()
progress=ttk.Progressbar(master=window,maximum=20,length=300,orient='vertical',variable=slider_var,mode='determinate')
progress.pack()

label=ttk.Label(master=window,textvariable=slider_var)
label.pack()

Slider=ttk.Scale(master=window,length=300,orient='horizontal',variable=slider_var,from_=0, to=20)
Slider.pack()

progress.start()
#run 
window.mainloop()