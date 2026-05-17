import tkinter as tk 
import ttkbootstrap as ttk 

#window 
window=ttk.Window(themename="journal")
window.title('Tab widget')
window.geometry('600x400')
#widgets 
notebook=ttk.Notebook(master=window)

#tab1
tab1 = ttk.Frame(master=notebook)
Label1 = ttk.Label(master=tab1, text='text in tab1')
Label1.pack()
button1 =ttk.Button(master=tab1, text='button in tab1', command=lambda: print("button has been pressed"))
button1.pack()

#tab2
tab2 = ttk.Frame(master=window)
Label2=ttk.Label(master=tab2, text='text in tab2')
Label2.pack()
entry_2=ttk.Entry(master=tab2)
entry_2.pack()

#tab 3
tab3= ttk.Frame(master=window)
label_3=ttk.Label(master=tab3, text='do you like scratch' )
radio_var =ttk.IntVar()
radio_1=ttk.Radiobutton(master=tab3,text= "yes", value="A1", variable=radio_var)
radio_2=ttk.Radiobutton(master=tab3,text="no", value="A2", variable=radio_var)
radio_1.pack()
radio_2.pack()
label_3.pack()


notebook.add(tab1, text='tab1')
notebook.add(tab2, text='tab2')
notebook.add(tab3, text='tab3')
notebook.pack()

#run 
window.mainloop()
