import tkinter as tk 
from tkinter import ttk 

# window
window = tk.Tk()
window.geometry('600x400')
window.title('layout intro')

# widgets 
label1 = ttk.Label(master=window, text = 'label 1 ', background='red')
label2 = ttk.Label(master=window, text = 'label 2 ', background='blue')

#pack 
label1.pack(side ='left', expand=True, fill = 'both') # expand = True makes it take up all the space
label2.pack(side ='right') #fill = both or x or y



#run 
window.mainloop()