import tkinter as tk 
import ttkbootstrap as ttk

# window
window = ttk.Window(themename='darkly')
window.title('Chrochet MAMA')
window.geometry('450x600')


method = ttk.StringVar(value="none")

def next_page():
    current = notebook.index(notebook.select())
    notebook.select(current + 1)

def previous_page():
    current = notebook.index(notebook.select())
    notebook.select(current - 1)

def next_page_method():
    if method.get() != 'none':
        next_page()

def delivery():
    method.set("deliver")
    label2.config(text=f'you have chosen {method.get()}')

def pickup():
    method.set("pickup")
    label2.config(text=f'you have chosen {method.get()}')

# notebook
notebook = ttk.Notebook(master=window)
notebook.pack(expand=True, fill='both')

# ---------- TAB 1 ----------
tab1 = ttk.Frame(master=notebook)

label1 = ttk.Label(tab1, text="would you like delivery or pickup services ? ",
                   font="Calibri 13 bold")
label1.pack(pady=10)

delivery_frame = ttk.Frame(tab1)
delivery_frame.pack(pady=20)

button1 = ttk.Button(delivery_frame, text='delivery', bootstyle='danger', command=delivery)
button2 = ttk.Button(delivery_frame, text='pickup', bootstyle='danger', command=pickup)
button1.pack(side='left', padx=10, pady=20)
button2.pack(side='right', padx=10, pady=20)

label2 = ttk.Label(tab1, text=f'you have chosen {method.get()}')
label2.pack()

button3 = ttk.Button(tab1, text="next", command=next_page_method)
button3.pack(pady=10, padx=10, side='right')

# ---------- TAB 2 ----------
tab2 = ttk.Frame(notebook)

# frame for menu items (takes most of the space)
menu_frame = ttk.Frame(tab2)
menu_frame.pack(fill='both', expand=True)

class menu(ttk.Frame):
    def __init__(self, parent, text, price):
        super().__init__(master=parent)
        self.text = text
        self.price = price

        ttk.Checkbutton(self).grid(row=0, column=0)
        ttk.Label(self, text=self.text).grid(row=0, column=1, columnspan=2)
        ttk.Label(self, text=self.price).grid(row=0, column=3, columnspan=2)

        self.pack(pady=5, anchor='w')

# items
menu(menu_frame, "sushi", "$18.78")
menu(menu_frame, "carrot", "$2")
menu(menu_frame, "ramen", "$14.50")
menu(menu_frame, "beef burger", "$12.90")
menu(menu_frame, "apple pie", "$5.20")
menu(menu_frame, "fried rice", "$10.00")
menu(menu_frame, "orange juice", "$3.80")
menu(menu_frame, "steak", "$22.40")
menu(menu_frame, "ice cream", "$4.60")
menu(menu_frame, "tacos", "$9.75")

# bottom button frame (always visible)
button_frame = ttk.Frame(tab2)
button_frame.pack(fill='x')

button5 = ttk.Button(button_frame, text="previous", command=previous_page)
button5.pack(pady=5, padx=10, side='left')

button4 = ttk.Button(button_frame, text="next", command=next_page)
button4.pack(pady=5, padx=10, side='right')

# add tabs
notebook.add(tab1, text="delivery options")
notebook.add(tab2, text="menu")

# run
window.mainloop()