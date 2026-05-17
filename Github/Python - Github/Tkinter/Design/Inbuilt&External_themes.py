import tkinter as tk
from tkinter import ttk , font

#window
window=tk.Tk()
window.title("Styling")
window.geometry('400x300')


#style
style = ttk.Style()
#style.theme_use('clam')

style.configure('Tbutton', background ='red')

#widgets 
label = ttk.Label(master =  window, text = 'A label \n And then type on another line',
                   background='red', 
                   foreground="white", 
                   font = ('Jokerman', 20), 
                   justify = 'center')
label.pack()

button = ttk.Button(master = window, text = 'A button')
button.pack()

#run 
window.mainloop()