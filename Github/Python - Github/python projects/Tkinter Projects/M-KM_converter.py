import  tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def Convert():
    mile_input = entry_int.get()
    km_input = mile_input * 1.61
    new_output = f'{km_input}km'
    output_string.set(new_output)

#Window
window=ttk.Window(themename='cyborg')# newer and more clean than tk.Tk()
# all theme names:'cosmo', 'flatly','litera,'minty','lumen','sandstone','yeti','pulse','united','morph','journal','darkly',superhero','solar','cyborg','vapor','simplex',cereculean'
window.title("Akain first app")
window.geometry("300x150")

#Label
# Label=ttk.Label(master,text,font(optional))
title_label=ttk.Label(master=window,text="Miles to Kilometers", font="Calibri 24 bold")
title_label.pack()#puts it in screeen

# input field
input_frame =ttk.Frame(master=window)
entry_int = tk.IntVar()
Entry =ttk.Entry(master=input_frame, textvariable= entry_int)
Button=ttk.Button(master=input_frame,text="Convert", command=Convert)
Entry.pack(side="left",padx=10)
Button.pack(side="left")
input_frame.pack(pady=10)

#Output
output_string=tk.StringVar()
output_label=ttk.Label(master=window,text="output", font="Calibri 24 bold", textvariable=output_string)
output_label.pack(pady=5)

#run 
window.mainloop()