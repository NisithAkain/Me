import customtkinter as ctk
from random import choice


class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master = parent)

        # general attributes
        self.start_pos = start_pos +0.05
        self.end_pos = end_pos
        self.width = abs(start_pos - end_pos)

        #animation logic
        self.pos = self.start_pos
        self.in_start_pos = True

        
        self.place(relx= self.start_pos, rely=0.05, relwidth = self.width, relheight = 0.9)

    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(relx= self.pos, rely=0.05, relwidth = self.width, relheight = 0.9)
            self.after(10, self.animate_forward)

        else:
            self.in_start_pos = False

    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.place(relx= self.pos, rely=0.05, relwidth = self.width, relheight = 0.9)
            self.after(10, self.animate_backwards)

        else:
            self.in_start_pos = True


# can only use place for animating widgets
def move_btn():
    global button_x
    button_x += 0.001
    print(button_x)
    button.place(relx=button_x, rely =0.5, anchor ='center')
    button.place(relx = button_x, rely = 0.5, anchor = 'center')
    if button_x < 0.9:
        window.after(10, move_btn)

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
ctk.set_appearance_mode('light')


#animated widget
animated_panel = SlidePanel(window,0,-0.3)
ctk.CTkLabel(animated_panel, text = "label 1 ").pack(expand = True, fill ='both', padx=2, pady =10)
ctk.CTkButton(animated_panel, text = "Button").pack(expand = True, fill ='both', padx=2, pady =10)
ctk.CTkLabel(animated_panel, text = "label 2 ", corner_radius=0).pack(expand = True, fill ='both', padx=0, pady =10)
ctk.CTkTextbox(animated_panel, fg_color= ('#dbdbdb', '#2b2b2b')).pack(expand = True, fill ='both')

#button
button_x=0.5
button = ctk.CTkButton(window,text = 'toggle sidebar', command = animated_panel.animate)
button.place(relx=button_x, rely =0.5, anchor ='center')

#run 
window.mainloop()