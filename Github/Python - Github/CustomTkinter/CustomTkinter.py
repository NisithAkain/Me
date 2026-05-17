import customtkinter as ctk 


#window
window = ctk.CTk()
window.title("Customtkinter app")
window.geometry('600x400')

#widgets
label = ctk.CTkLabel(window, text = 'A ctk label', 
                     fg_color=("blue","red"), 
                     text_color='white', corner_radius=4)
label.pack()

button = ctk.CTkButton(window, text='a ctk button', fg_color= '#FF0',
                        text_color='#000', hover_color='#AA0',
                          command = lambda: ctk.set_appearance_mode('light'))
button.pack()
button2 = ctk.CTkButton(window, text='a ctk button',
                         fg_color= '#FF0', text_color='#000',
                           hover_color='#AA0', 
                           command = lambda: ctk.set_appearance_mode('dark'))

# fg colour = ("blue", "red") blue when light, red when dark
button2.pack()

frame = ctk.CTkFrame(master = window)#fg_color=transparent
frame.pack()

slider = ctk.CTkSlider(frame)
slider.pack(padx=20, pady=20)
   
#run
window.mainloop()