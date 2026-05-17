import tkinter as tk 
import ttkbootstrap as ttk 

#widnow
window = ttk.Window(themename='darkly')
window.title('Spinbox')
window.geometry('600x500')

#Spinbox
spin_var = ttk.StringVar()
spin = ttk.Spinbox(master=window, from_ =3, to= 20, increment=3, command= lambda: print("an arrow was pressed "), textvariable=spin_var)#goes up in 3's 
#spin['value']=[1,2,3,4,5]
spin.pack()
spin.bind('<<Increment>>', lambda event: label.config(text=f'Value was incremented current value:{spin_var.get()}'))
spin.bind('<<Decrement>>', lambda event: label.config(text=f'Value was dectremented current value:{spin_var.get()}'))

#label
label = ttk.Label(master=window, text='not set')
label.pack()
#run 
window.mainloop()

