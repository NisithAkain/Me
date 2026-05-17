import tkinter as tk 
from tkinter import ttk 
from random import randint,choice

#setup 
window = tk.Tk()
window.geometry('600x400')
window.title('Scrolling')

def hello():
    print("does things still work around here")

#canvas
canvas = tk.Canvas(master = window, bg='red', scrollregion=(0,0,2000,5000)) #scrollregion = (left, top, right , bottom)
canvas.create_line(0,0,2000,5000, fill='green', width = '10')#(0,0) start position , (2000, 5000) #end position
for i in range(100):
    left = randint(0,2000)
    top= randint(0,5000)
    right= left + randint(10,500)
    bottom = top +  randint(10,500)
    color = choice(('red', 'green', 'blue', 'yellow', 'orange'))
    canvas.create_rectangle(left,top,right,bottom, fill = color)
canvas.pack(expand=True, fill='both')

#mousewheel scrolling 
canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(-int(event.delta/60),"units")) #always going to be "units" other one is the amount in which you scroll
canvas.bind('<Control MouseWheel>', lambda event: canvas.xview_scroll(-int(event.delta/60),"units"))
# delta value is how much and which way mousewheel is moving

#scrollbar
scrollbar = ttk.Scrollbar(master=window, orient='vertical',command=canvas.yview)#so that scrollbar influenze the canvas
canvas.configure(yscrollcommand=scrollbar.set)# so that canvas influenze the scrollbar
scrollbar.place(relx =1, rely=0, relheight=1, anchor='ne')

scrollbarX = ttk.Scrollbar(master=window, orient = 'horizontal', command = canvas.xview)
canvas.configure(xscrollcommand=scrollbarX.set)
scrollbarX.place(relx = 0, rely =1,relwidth = 1, anchor=  'sw' )

hello()

#run 
window.mainloop()