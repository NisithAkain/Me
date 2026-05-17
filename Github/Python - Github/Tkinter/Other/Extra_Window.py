import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox

def ask_yes_no():
    #answer = messagebox.askquestion('Title', 'body')
    #print(answer)
    #messagebox.showinfo('Info title ', 'here is some info')
    messagebox.showerror('Mcafee Security Alert','Warning: Macafee could not scan this file syntax trace 10htt#2 error 2012')

def create_window():
    global extra_window
    extra_window=tk.Toplevel()
    extra_window.title('extra window')
    extra_window.geometry('300x400')
    ttk.Label(master = extra_window, text = 'A label').pack()
    ttk.Button(master = extra_window, text = 'A Button').pack()        


def close_window():
    extra_window.destroy()
 

    

#window
window = tk.Tk()
window.title('Multiple Windows')
window.geometry('600x400')

button1 = ttk.Button(master=window, text='open main window', command = create_window)
button1.pack(expand = True)


button2 = ttk.Button(master = window,  text = "close main  window", command = close_window)
button2.pack(expand = True)


button3 = ttk.Button(master=window, text = 'create yes no window', command= ask_yes_no)
button3.pack(expand =True)

#run
window.mainloop()