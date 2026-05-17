import tkinter as tk
import ttkbootstrap as ttk 

#window 
window=ttk.Window(themename = 'darkly')
window.geometry('600x500')
window.title('Combobox')

#combobox
iteams = ['ice cream', 'pizza', 'brocoli']
food_string = ttk.StringVar(value=iteams[0]) # "Ice cream "
combo = ttk.Combobox(master=window, textvariable=food_string)
combo.pack()
combo['values']=iteams

#events{
combo.bind('<<ComboboxSelected>>', lambda event: Label.config(text= f'selected value:{food_string.get()}'))


#label
Label =ttk.Label(master=window, text = 'a label')
Label.pack()
#run 
window.mainloop()