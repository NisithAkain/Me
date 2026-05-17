import tkinter as tk 
import ttkbootstrap as ttk 

#setup 
window = ttk.Window(themename='journal')
window.title('Checkbuttons ')
window.geometry('600x400')

# variable 
check_var = ttk.IntVar() #could use either strint or Int but bool is more intuitive
#checkbutton
check=ttk.Checkbutton(master=window, text='checkbox 1',command=lambda:print(check_var.get()), variable=check_var, onvalue=1 , offvalue =0 )
# in checkboxes there is no "textvariable" but instead "variable", onvalue is the value returns when on and offvalue viseversa 
check.pack()

#run 
window.mainloop()