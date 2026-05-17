import tkinter as tk 
import ttkbootstrap as ttk 
from ttkbootstrap.toast import ToastNotification

#window
window = ttk.Window()
window.title('toast ')

#toast, a notification 
toast = ToastNotification(title='this is a messgae title', 
                         message='this is the accual message ',
                         duration = 2000, bootstyle='dark', position=(10,10,'ne')) #position = (x padding, ypadding, start pos('se'))
# duration in in milliseconds

#toast.show_toast()   #this shows the toast,
# when left by itself without function it buggs everthing else


ttk.Button(master = window, text = 'toast', command = toast.show_toast).pack() #now it is good because it s in a function 

#run 
window.mainloop()