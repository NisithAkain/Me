import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('place')
window.geometry('400x600')

#widgets 
label1=ttk.Label(master = window, text = 'Label1', background = 'red')
label2=ttk.Label(master = window, text = 'Label2', background = 'blue')
label3=ttk.Label(master=window, text = 'Label3', background = 'green')
button1 = ttk.Button(master = window, text = 'Button1')

#layout 
label1.place( x = 300, y=100, width = 100, height = 200 )
label2.place(relx =0.2, rely=0.2, relwidth = 0.4, relheight =0.5)
label3.place(x = 100, y=100, width =100, height =100)
button1.place(relx=0.1, rely=0.1, relwidth=0.2, anchor ='center' )

label1.lift() # makes it go up a layer
label3.lower() # makes it go down a layer

button1.lift(aboveThis = label3) # will be above label3


#run 
window.mainloop()