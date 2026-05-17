import tkinter as tk 
from tkinter import ttk 

# window
window = tk.Tk()
window.geometry('400x600')
window.title('pack')

#widgets 
label1 = ttk.Label(master =window, text='First label', background = 'red')
label2 = ttk.Label(master =window, text='Label 2 ', background = 'blue')
label3 = ttk.Label(master =window, text='Last of the labels', background = 'green')
button = ttk.Button(master = window, text = 'Button')

# layout 
label1.pack(side= 'top', expand=  True)
label2.pack(side = 'top')
label3.pack(side ='top')
button.pack(side = 'top', expand = True)


#run 
window.mainloop()