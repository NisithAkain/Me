import tkinter 
import ttkbootstrap as ttk

#define
def show():
    print(show_var.get())

#window
window = ttk.Window(themename = 'journal')
window.geometry('400x600')
window.title('rip off paulse')

#widgets
Notebook= ttk.Notebook(master=window)

#tab 1 
tab1 = ttk.Frame(master= window)
show_var = ttk.IntVar()
label1 = ttk.Label(master = tab1, text = 'which of the following describes how you feel')
Slider1 = ttk.Scale(master= tab1, length = 200, from_=0, to = 10,orient='horizontal',variable=show_var, command = show() )
label1.pack()
Slider1.pack(expand =True, fill = 'both')



tab2 = ttk.Frame(master= window)
tab3 = ttk.Frame(master = window)

#Notebook.add
Notebook.add(tab1, text='Feeling')
Notebook.pack()

#run 
window.mainloop()