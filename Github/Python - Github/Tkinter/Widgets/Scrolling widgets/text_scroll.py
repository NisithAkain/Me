import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('Scrolling')
window.geometry('600x400')


#text
text = tk.Text(master=window)
for i in range (200):
    text.insert(f'{i}.0', f'text:{i} \n')
text.pack(expand = True,fill='both')

scrollbar_text = ttk.Scrollbar(master=window, orient='vertical',command=text.yview)#so that scrollbar influenze the canvas
text.configure(yscrollcommand=scrollbar_text.set)# so that canvas influenze the scrollbar
scrollbar_text.place(relx =1, rely=0, relheight=1, anchor='ne')

#run 
window.mainloop()