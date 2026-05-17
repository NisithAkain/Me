import tkinter as tk 
from tkinter import ttk 

class Segment(ttk.Frame):
    def __init__(self, parent, label_text, button_text):
        super().__init__(master = parent)

        # grid layout 
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0,1,2), weight=1, uniform = 'a')
        ttk.Label(self, text =label_text).grid(row=0, column=0, sticky ='nsew')
        ttk.Button(self, text=button_text).grid(row=0, column=1, sticky = 'nsew')

        self.pack(expand=True, fill='both',padx=10, pady=10)


#window
window = tk.Tk()
window.title('widgets and return ')
window.geometry('400x600')

#widgets 
Segment(window, 'label', 'button')
Segment(window, 'test', 'click')
Segment(window, 'hello', 'test')
Segment(window, 'bye', 'launch')
Segment(window, 'last one', 'test')



#run 
window.mainloop()