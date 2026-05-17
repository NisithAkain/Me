import customtkinter as ctk
from random import choice

# can only use place for animating widgets
def move_btn():
    global button_x
    button_x += 0.05
    print(button_x)
    button.place(relx=button_x, rely =0.5, relheight = button_x, anchor ='center')

    #configure 
    colors = ['red', 'yellow', 'pink', 'green', 'blue', 'black', 'white']
    color = choice(colors)
    button.configure(fg_color = color)

#after
def infinite_print():
    global button_x
    button_x+=0.5
    print('infinite')
    print(button_x)
    if button_x <10:
        window.after(1000, infinite_print) # aftter 1 sec it sends infinite print

#window
window= ctk.CTk()
window.title('Animated Widgets')
window.geometry('600x400')

#button
button_x=0.5
button = ctk.CTkButton(window,text = 'toggle sidebar', command = infinite_print)
button.place(relx=button_x, rely =0.5, anchor ='center')

#run 
window.mainloop()