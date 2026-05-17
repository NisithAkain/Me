# canvas lets you draw shapes
import tkinter as tk 
import ttkbootstrap as ttk 

# window
window = ttk.Window(themename='journal')
window.title('Canvas')
window.geometry('600x400')

#canvas
canvas = ttk.Canvas(master=window, bg='white')
canvas.pack()

canvas.create_rectangle((20,20,100,200), fill='red', width=10, dash=(1,2,3), outline='green') #(x1,y1,x2,y2)
canvas.create_oval((0,0,100,100), fill='green')#(left, top, right, bottom)


canvas.create_line((0,0,100,150), fill='blue', width=10)#(start_x,start_y, end_x, end_y)
canvas.create_polygon((200,300,150,89,76,100), fill='black') # can go forever(x1,y1,x2,y2,... xn,yn ) create n-sides polygon 
#(0,0) is top left of canvas so numbers go outward form origin

canvas.create_text((200,200), text = 'some text', fill ='turquoise')

canvas.create_window((50,50), window = ttk.Label(master=window, text = " a label iside a canvas"))
#run 
window.mainloop()
