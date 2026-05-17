import tkinter as tk 
from tkinter import ttk

#window
window =tk.Tk()
window.geometry('400x600')
window.title('pack_fill exercise 1')

#widgets 
label1 = ttk.Label(master =window,text ='label 1', background = 'red')
label2 = ttk.Label(master =window, text ='label 2', background = 'blue')
label3 = ttk.Label(master =window,text = 'label3', background = 'green')
label4 = ttk.Label(master =window, text='label4' )

#pack 
label1.pack(side ='top', fill = 'x')
label2.pack(side = 'top', expand = True)
label3.pack(side='top', fill = 'both', expand =True)
label4.pack(side = 'top', fill = 'x')



#run 
window.mainloop()