import tkinter as tk 
from tkinter import ttk
import customtkinter as ctk 
from PIL import Image, ImageTk

#setup
window = tk.Tk()
window.geometry('600x400')
window.title('Images') 

#grid layout
window.columnconfigure((0,1,2,3), weight=1, unifor ='a')
window.rowconfigure(0, weight =1)


#import an image 
image_original = Image.open(r'C:\Users\Me\Downloads\raccoon.jpg').resize((600,400))
image_tk=ImageTk.PhotoImage(image_original)

python_dark = Image.open(r'C:\Users\Me\Downloads\dark&light.png').resize((30,30))
python_dark_tk = ImageTk.PhotoImage(python_dark)
image_ctk = ctk.CTkImage(light_image= Image.open(r'C:\Users\Me\Downloads\dark&light.png'), dark_image= Image.open(r'C:\Users\Me\Downloads\dark&light.png'))#for ctk we need for dark and light 

#widget
#label = ttk.Label(window, text = 'racoon', image=image_tk)
#label.pack() 
button_frame = ttk.Frame(window)
button = ttk.Button(button_frame, text = '   light/dark', image = python_dark_tk, compound ='left')# this is so that the image and the text are visibe
button.pack(pady =10)

button_ctk = ctk.CTkButton(button_frame, text = '   light/dark', image = image_ctk, compound ='left')# this is so that the image and the text are visibe
button_ctk.pack(pady=10)

button_frame.grid(column =0, row =0 , sticky = 'nsew')


#canvas --> image 


#run 
window.mainloop()

