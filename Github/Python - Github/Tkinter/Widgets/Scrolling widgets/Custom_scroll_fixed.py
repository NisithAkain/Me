import tkinter as tk
from tkinter import ttk


class ListFrame(ttk.Frame):
    def __init__(self, parent, text_data, item_height):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')

        # widget data
        self.text_data = text_data
        self.item_number = len(text_data)
        self.list_height = self.item_number * item_height

        # canvas
        self.canvas = tk.Canvas(self, background='red')
        self.canvas.pack(side='left', expand=True, fill='both')

        # scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # inner frame inside canvas
        self.frame = ttk.Frame(self.canvas)
        self.window_id = self.canvas.create_window((0, 0), window=self.frame, anchor='nw')

        # populate
        for index, item in enumerate(self.text_data):
            self.create_item(index, item).pack(fill='x', pady=4, padx=10)

        # bindings: when inner frame changes size, update scrollregion
        self.frame.bind('<Configure>', self._on_frame_configure)
        # when canvas changes size, make inner frame width match
        self.canvas.bind('<Configure>', self._on_canvas_configure)
        # mouse wheel (Windows: delta is multiple of 120)
        self.canvas.bind_all('<MouseWheel>', lambda event: self.canvas.yview_scroll(-int(event.delta / 120), 'units'))

    def _on_frame_configure(self, event):
        # update scrollable region to fit inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def _on_canvas_configure(self, event):
        # make the inner frame match the canvas width
        self.canvas.itemconfig(self.window_id, width=event.width)

    def create_item(self, index, item):
        frame = ttk.Frame(master=self.frame)

        # grid layout
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')

        # widgets
        ttk.Label(master=frame, text=f'#{index}').grid(row=0, column=0)
        ttk.Label(master=frame, text=f'{item[0]}').grid(row=0, column=1)
        ttk.Button(master=frame, text=f'{item[1]}').grid(row=0, column=2, columnspan=3, sticky='nsew')

        return frame



# window
window = tk.Tk()
window.geometry('500x400')
window.title('Custom Widget Scrolling')

text_list = [('label', 'evil'), ('peppa', 'aggro'), ('akain', 'kind'),
             ('john', 'brave'), ('doe', 'smart'),
             ('alice', 'curious'), ('bob', 'funny'), ('charlie', 'cheerful'),
             ('dave', 'strong'), ('eve', 'sneaky')] * 10
list_frame = ListFrame(window, text_list, 100)


# RUN
window.mainloop()
