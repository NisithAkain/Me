import tkinter as tk 
import ttkbootstrap as ttk 

#window 
window = ttk.Window()
window.title('paint app')
window.geometry('600x500')

#define
def draw_on_canvas(event):
    x=event.x
    y=event.y
    canvas.create_oval((x-brushsize/2,y-brushsize/2,x+brushsize/2,y+brushsize/2), fill ='black')

brushsize = 2
#canvas 
canvas = ttk.Canvas(master=window)
canvas.pack()
canvas.bind('<Motion>', draw_on_canvas)


#run 
window.mainloop()