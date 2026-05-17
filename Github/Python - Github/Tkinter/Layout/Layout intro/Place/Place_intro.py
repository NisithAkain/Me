import tkinter as tk 
from tkinter import ttk 

# window
window = tk.Tk()
window.geometry('600x400')
window.title('layout intro')

# widgets 
label1 = ttk.Label(master=window, text = 'label 1 ', background='red')
label2 = ttk.Label(master=window, text = 'label 2 ', background='blue')

#place 
label1.place(x=100, y=200, width = 200, height = 100 ) # could come of screen if too big 
label2.place(relx=0.5 , rely =0.5, relwidth = 1, relheight = 2, anchor = 'se')# s n w e se ..etc 
# always stays in the relative position 


#run 
window.mainloop()