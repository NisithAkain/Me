
import tkinter as tk 
import ttkbootstrap as ttk

def button_func():
    print('a button was pressed')

def button2_func():
    print("hello")



# tab 1 
tab1= ttk.Frame
#window 
window=ttk.Window(themename='darkly')
window.title("Window and Widgets ")
window.geometry('600x600')

#ttk Label
label=ttk.Label(master=window,text='this is a test')
label.pack()

#ttk text
text= ttk.Text(master=window)
text.pack()

#ttk entry 
entry =ttk.Entry(master=window)
entry.pack()


#ttk button
button=ttk.Button(master=window,text="a button ", command=button_func, )
button.pack()

#ttk radio buttons 
radio_var = ttk.StringVar()
radio1 = ttk.Radiobutton(master=window,text='hello',variable=radio_var, value='A1')
radio2 = ttk.Radiobutton(master=window,text='world',variable=radio_var, value='A2')
radio3 = ttk.Radiobutton(master=window,text='galaxy', variable=radio_var, value='A3')
radio1.pack()
radio2.pack()
radio3.pack()

#ttk ckeckbuttons 
check =ttk.Checkbutton(master=window, text='happy')
check.pack()

#ttk combobox 
iteams=['tkinter','pygame','Numpy']
combo = ttk.Combobox(master=window)
#combo.config(values=iteams)
combo['values']=iteams
combo.pack()

#ttk SpinboxBox
spin = ttk.Spinbox(master=window, from_ = 1, to=20, increment=2)
spin.pack()

#ttk slider
slider_var=ttk.DoubleVar(value=10)
slider=ttk.Scale(
    master=window,
    from_=0,to=20,
    variable=slider_var,
    length=500,
    orient='horizontal')

#ttk progress 
progress=ttk.Progressbar(
    master=window,
    maximum=20,
    length=400,
    orient='horizontal'
    ,variable=slider_var)
progress.pack()
slider.pack()

# run 
tk.mainloop()