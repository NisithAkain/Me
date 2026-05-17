import customtkinter as ctk


items = 11

#window
window = ctk.CTk()
window.geometry('700x700')
window.title('My Time table app')
window.minsize(height=600, width=600)

global edit
edit = ctk.IntVar(value=0)







class Elements(ctk.CTkFrame):
    def __init__(self, parent, text, butn):
        super().__init__(parent)
        self._corner_radius = 5
        self.text_var = ctk.StringVar(value=text)
        self.editing = False
        self.columnconfigure(0, weight=3, uniform='a')
        self.columnconfigure(1, weight=1, uniform='a')
        self.rowconfigure(0, weight=1)

        if butn == 0:
            self.display_label()
            self.check = ctk.CTkCheckBox(master=self, text="Done")
            self.check.grid(row=0, column=1, sticky='nsew', padx=10)
            self.edit_btn = ctk.CTkButton(self, text="Edit", width=60, command=self.toggle_edit)
            self.edit_btn.grid(row=0, column=2, sticky='nsew', padx=5)
        else:
            # For the last row, just show a button (if needed)
            self.button = ctk.CTkButton(self, text=text, command=self.toggle_edit)
            self.button.grid(row=0, column=0, sticky='nsew', padx=10)

    def display_label(self):
        # Remove entry if exists
        if hasattr(self, 'entry') and self.entry is not None:
            self.entry.destroy()
            self.entry = None
        # Remove label if exists
        if hasattr(self, 'label') and self.label is not None:
            self.label.destroy()
        self.label = ctk.CTkLabel(master=self, textvariable=self.text_var, font=("Calibri", 24))
        self.label.grid(row=0, column=0, sticky='nsew')

    def display_entry(self):
        # Remove label if exists
        if hasattr(self, 'label') and self.label is not None:
            self.label.destroy()
        # Remove entry if exists
        if hasattr(self, 'entry') and self.entry is not None:
            self.entry.destroy()
        self.entry = ctk.CTkEntry(master=self, textvariable=self.text_var, font=("Calibri", 24))
        self.entry.grid(row=0, column=0, sticky='nsew')
        self.entry.focus_set()

    def toggle_edit(self):
        if not self.editing:
            self.display_entry()
            self.editing = True
            if hasattr(self, 'edit_btn') and self.edit_btn is not None:
                self.edit_btn.configure(text="Save")
            if hasattr(self, 'button') and self.button is not None:
                self.button.configure(text="Save")
        else:
            self.display_label()
            self.editing = False
            if hasattr(self, 'edit_btn') and self.edit_btn is not None:
                self.edit_btn.configure(text="Edit")
            if hasattr(self, 'button') and self.button is not None:
                self.button.configure(text="Edit")




window.rowconfigure((0,1,2,3,4,6,7,8,9,10,11,12), weight=1)
window.columnconfigure(0, weight=1)

Screen=window


e1 = Elements(Screen, "Wake up at 5:00am",0)
e1.grid(column=0, row=0, sticky = 'nsew', padx = 10, pady=10, )

e2 = Elements(Screen, "5am-6am: 1hour science",0)
e2.grid(column=0, row=1, sticky = 'nsew', padx=10, pady=10)

e3 = Elements(Screen, "6am-7am: 1hour maths",0)
e3.grid(column=0, row=2, sticky = 'nsew', padx=10, pady=10)

e4 = Elements(Screen, "5am-6am: 1hour science",0)
e4.grid(column=0, row=3, sticky = 'nsew', padx=10, pady=10)

e5 = Elements(Screen, "School",0)
e5.grid(column=0, row=4, sticky = 'nsew', padx=10, pady=10)

e6 = Elements(Screen, "4pm-5pm: 1hour maths",0)
e6.grid(column=0, row=5, sticky = 'nsew', padx=10, pady=10)

e7 = Elements(Screen, "5pm-6pm: 1hour python",0)
e7.grid(column=0, row=6, sticky = 'nsew', padx=10, pady=10)

e8 = Elements(Screen, "30min break",0)
e8.grid(column=0, row=7, sticky = 'nsew', padx=10, pady=10)

e9= Elements(Screen, "6:30pm-7:30pm: 1hour science",0)
e9.grid(column=0, row=8, sticky = 'nsew', padx=10, pady=10)

e10 = Elements(Screen, "7:30-8:30: 1hour Arduino",0)
e10.grid(column=0, row=9, sticky = 'nsew', padx=10, pady=10)

e11 = Elements(Screen, "8:30-9:30: read",0)
e11.grid(column=0, row=10, sticky = 'nsew', padx=10, pady=10)



#run 
window.mainloop()