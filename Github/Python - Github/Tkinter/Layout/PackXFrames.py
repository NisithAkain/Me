import tkinter as tk
import ttkbootstrap as ttk

#window
window= ttk.Window(themename ='journal')
window.title('pack parenting')
window.geometry('400x600')

#Top frame
top_frame = ttk.Frame(master = window)
label1 = ttk.Label(master = top_frame, text = 'First Label', background='red')
label2 = ttk.Label(master = top_frame, text = 'Label 2 ', background = 'blue')

#Middle widgets
label3 = ttk.Label(master= window, text = 'another window', background = 'green')

#bottom frame
bottom_frame = ttk.Frame(master= window)
label4 = ttk.Label(master = bottom_frame, text ='last of the labels', background = 'orange')
button = ttk.Button(master = bottom_frame, text = 'A button')
button2 = ttk.Button(master=bottom_frame, text = 'Another Button')

#Top layout
label1.pack(side = 'left', fill='both', expand = True)
label2.pack(side = 'left', fill='both', expand = True)
top_frame.pack(fill ='both', expand = True)

#middle layout
label3.pack(expand = True)

#bottom layout
button.pack(side = 'left', expand= True, fill = 'both')
label4.pack(side = 'left', expand = True, fill ='both')
button2.pack(side = 'left', expand = True, fill = 'both')
bottom_frame.pack(expand=True, fill = 'both', padx = 20, pady=20)

#run 
window.mainloop()
