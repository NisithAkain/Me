import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tbk
from tkinter import messagebox



def start_download():
    Macfee_Widget.grid_forget()
    Context.grid_forget()
    global percentage
    global scale
    for percentage in range(0,100):
        scaleInt = tk.IntVar(value =0 )
        scale = ttk.Scale(master =window, orient = 'horizontal', variable = scaleInt)
        scale.grid()
    

def show_download():
    Button.grid_forget()
    global download
    download = ttk.Button(master = window, text = "start download",  command = start_download).grid(row = 3 , column=4, padx = 10)

def button_func():
    if  radiovar.get() ==  0:
        pass

    if radiovar.get() == 1:
        for i in range(1,3):
            messagebox.showinfo('Macafee Support', 'This task could not be completed')
        messagebox.showerror('Mcafee Security Alert','Warning: Macafee could not scan this file syntax trace 10htt#2 error 2012')
        radiobutton.grid_forget()
        ContextVar.set(value='To gain autorotization into your Mcafee account \n please proceed with the download')
        show_download()

#window
window = tbk.Window(themename='darkly')
window.geometry('400x500')
window.minsize(height=300, width=500)
window.maxsize(height=300, width=500)
window.title('Macafee Antivirus')

#widgets 
Macfee_Widget = ttk.Label(master = window, text = "Macafee Alert", font = ("Arial", 15), foreground = "#ff6666")
Macfee_Widget.grid(row = 0, column=0,  sticky = 'w', padx=20)


ContextVar = tk.IntVar(value = "System Status: Potential Compromise\n"
        "Unusual remote activity has been detected on this device.\n"
        "Some system functions may be restricted until verification.\n"
        "To continue, please proceed.")
Context = ttk.Label(
    master=window,textvariable=ContextVar,
    text=(
        "System Status: Potential Compromise\n"
        "Unusual remote activity has been detected on this device.\n"
        "Some system functions may be restricted until verification.\n"
        "To continue, please proceed."), font = ("Arial", 10)
)
Context.grid(row=1, column=0, columnspan=2)


radiovar = tk.IntVar(value = 0)
radiobutton = ttk.Radiobutton(master = window,text = "I agree and want to continue", value = 1 , variable= radiovar)
radiobutton.grid(row = 2, column = 0 )


Button = ttk.Button(master= window, text = "Next", command = button_func)
Button.grid(row = 3 , column=4, padx = 10)

#grid 
window.rowconfigure((0,1,2,3), weight = 1 )
window.columnconfigure((0,1,2), weight= 1 )


print("System Status: potention Copromise Unusual remote activity has been detected on this device.Some system functions may be resticted until verification is completed. To continue, please continue")



#run 
window.mainloop()