import tkinter as tk 
import ttkbootstrap as ttk 

def get_pos(event):
    print(f'x{event.x} y{event.y}')

# setup 
window = ttk.Window(themename='cyborg')

#widgets
text =ttk.Text(master=window)
text.pack()
entry_string = ttk.StringVar()
entry= ttk.Entry(master=window,textvariable=entry_string)
entry.pack()

btn = ttk.Button(master=window, text = 'a button')
btn.pack()

#events
btn.bind('<Alt-KeyPress-a>', lambda event: print("an event"))  #window.bind(event('modifyer-type-detail'), function)
#window.bind('<Motion>', get_pos)
entry.bind('<FocusIn>', lambda event: print('mouse is hovering over entry field'))

#run 
window.mainloop()