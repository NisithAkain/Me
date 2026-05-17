import tkinter as tk 
import ttkbootstrap as ttk 
from ttkbootstrap.widgets import DateEntry, Meter, ToastNotification
from tkinter import messagebox

# FUNCTIONS 
def shift_Notebook():
    current = Notebook.index(Notebook.select())
    Notebook.select(current+1)

#window
window = ttk.Window(themename = 'darkly')
window.geometry('600x350')
window.title("paulse app")

#widgets 
Notebook = ttk.Notebook(master = window)
Notebook.pack(expand = True, fill ='both')


#welcome
welcome_tab =  ttk.Frame(master = Notebook)
welcome_message = ttk.Label(welcome_tab, text = " Welcome user please answer the following questions to proceed \n by continuing you are agreeing to the following atatements \n > you will let us use your data to give to goverment \n > use previous forms to better target questions tow ards you " ,font =("Segoe UI", 10))
welcome_message.pack(pady =20)
welcome_date = ttk.DateEntry(welcome_tab)
welcome_date.pack()
welcome_button = ttk.Button(welcome_tab, text = "Continue and agree", command = shift_Notebook)
welcome_button.pack(pady=30 ,fill = 'y')

# gender 
def gender_completed():
    if gender != 0:
        shift_Notebook
    elif gender == 0 :
        #Toast1 = ToastNotification(message="you have not fully completed the form", duration = 1000, bootstyle='danger')
        #Toast1.show_toast()
        messagebox.showerror('We could not properly subbmit this data')


gender_tab = ttk.Frame(master = Notebook)
gender_text = ttk.Label(gender_tab, text = "what gender are you?", font =("Segoe UI", 14))
gender_text.pack(pady = 20)
gender = ttk.IntVar(value = 0)
gender_radio1 = ttk.Radiobutton(gender_tab, text = "  male", value =1, variable = gender)
gender_radio2 = ttk.Radiobutton(gender_tab, text = "female", value =2,  variable = gender)
gender_radio1.pack(pady=20)
gender_radio2.pack()
gender_button = ttk.Button(gender_tab, text = "next", command =shift_Notebook)
gender_button.pack(side = 'right', pady = 30, padx=10)

#name
name_tab = ttk.Frame(Notebook)
name_text = ttk.Label(name_tab, text = "whats your first name?", font =("Segoe UI", 14))
name_text.pack(pady=20)
name_entry1 = ttk.Entry(name_tab)
name_entry1.pack(pady = 10)

name_text2 = ttk.Label(name_tab, text = "whats your last name?", font =("Segoe UI", 14))
name_text2.pack(pady=20)
name_entry2 = ttk.Entry(name_tab)
name_entry2.pack(pady = 10)
name_button = ttk.Button(name_tab, text = "next", command = shift_Notebook)
name_button.pack(side ='right', padx=10)

#meter
tab = ttk.Frame(Notebook)
text = ttk.Label(tab, text = "what number represents your happiness?", font =("Segoe UI", 14))
text.pack(pady=20)
meter = ttk.Meter(tab, interactive = True, amounttotal=10, amountused=0, metertype='semi')
meter.pack(pady=10)
button = ttk.Button(tab, text = "view report", command = shift_Notebook)
button.pack(side = 'right', padx=10)


# notebook add 
Notebook.add(welcome_tab, text = " welcome")
Notebook.add(gender_tab, text = "gender")
Notebook.add(name_tab, text = "name")
Notebook.add(tab, text = "Happy Meter")

#mainloop
window.mainloop()