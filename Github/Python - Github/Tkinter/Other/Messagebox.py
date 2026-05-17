import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox

def ask_yes_no():
    #answer = messagebox.askquestion('Title', 'body')
    #print(answer)
    #messagebox.showinfo('Info title ', 'here is some info')
    messagebox.showerror('Mcafee Security Alert','Warning: Macafee could not scan this file syntax trace 10htt#2 error 2012')



#window
window = tk.Tk()
window.title('Multiple Windows')
window.geometry('600x400')

button1 = ttk.Button(master=window, text='open main window')
button1.pack(expand = True)


button2 = ttk.Button(master = window,  text = "close main  window")
button2.pack(expand = True)


button3 = ttk.Button(master=window, text = 'create yes no window', command= ask_yes_no)
button3.pack(expand =True)

#run
window.mainloop()