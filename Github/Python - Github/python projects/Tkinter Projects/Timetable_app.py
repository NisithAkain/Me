import customtkinter as ctk

#window
window = ctk.CTk()
window.geometry('600x500')
window.title('My Time table app')
window.minsize(height=600, width=500)


class Elements(ctk.CTkFrame):
    def __init__(self, parent, text):
        super().__init__(parent)
        self._corner_radius=5
        self.columnconfigure(0, weight=3, uniform='a')
        self.columnconfigure(1, weight=1, uniform='a')
        self.rowconfigure(0, weight=1)

        self.text = text
        self.Label = ctk.CTkLabel(master=self, text=text, font=("Calibri", 24))
        self.Label.grid(row=0, column=0, sticky='nsew')

        self.check = ctk.CTkCheckBox(master = self, text = "Done").grid(row = 0, column= 1, sticky = 'nsew')

window.rowconfigure((0,1,2,3,4,6,7,8,9,10,11), weight=1)
window.columnconfigure(0, weight=1)



e1 = Elements(window, "Wake up at 5:00am")
e1.grid(column=0, row=0, sticky = 'nsew', padx = 10, pady=10, )

e2 = Elements(window, "5am-6am: 1hour science")
e2.grid(column=0, row=1, sticky = 'nsew', padx=10, pady=10)

e3 = Elements(window, "6am-7am: 1hour maths")
e3.grid(column=0, row=2, sticky = 'nsew', padx=10, pady=10)

e4 = Elements(window, "5am-6am: 1hour science")
e4.grid(column=0, row=3, sticky = 'nsew', padx=10, pady=10)

e5 = Elements(window, "School")
e5.grid(column=0, row=4, sticky = 'nsew', padx=10, pady=10)

e6 = Elements(window, "4pm-5pm: 1hour maths")
e6.grid(column=0, row=5, sticky = 'nsew', padx=10, pady=10)

e7 = Elements(window, "5pm-6pm: 1hour python")
e7.grid(column=0, row=6, sticky = 'nsew', padx=10, pady=10)

e8 = Elements(window, "30min break")
e8.grid(column=0, row=7, sticky = 'nsew', padx=10, pady=10)

e9= Elements(window, "6:30pm-7:30pm: 1hour science")
e9.grid(column=0, row=8, sticky = 'nsew', padx=10, pady=10)

e10 = Elements(window, "7:30-8:30: 1hour Arduino")
e10.grid(column=0, row=9, sticky = 'nsew', padx=10, pady=10)

e11 = Elements(window, "8:30-9:30: read")
e11.grid(column=0, row=10, sticky = 'nsew', padx=10, pady=10)



#run 
window.mainloop()