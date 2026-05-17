import tkinter as tk
from tkinter import ttk



#window
window = tk.Tk()
window.title('More on the window ')
window.geometry('600x400+100+100')  # 600x400+amount_horizontal + amount_vertical

# window sizes
window.minsize(200,100) # height, width 
window.maxsize(600,400) # heigt,  width 
window.resizable(True, False) # X, Y 

# Screen Stuff 
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

#window attributes 
window.attributes('-alpha', 1) # 0=transparent, 1=opaque
window.attributes('-topmost', True) # always be on top layer

#Security event 
window.bind('<Escape>', lambda event: window.quit())

#window.attributes('-disable', True)

# Title bar 
#window.overrideredirect(True) # tile bar invisible 
# grip = ttk.Sizegrip(window)
#grip.place(relx=1.0, rely= 1.0, anchor = 'se')

# run
window.mainloop()