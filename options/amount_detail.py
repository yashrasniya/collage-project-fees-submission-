from Frame.frameCommanThings import FrameCommonThings as f
from data import Data
from tkinter import *
from tkinter.ttk import *


class AM:
    def __init__(self, master):
        self.obj = Data.obj
        self.obj.table = Data.Amount_detail_table
        self.top = Toplevel(master)
        Label(self.top, text='semester').grid(row=0, column=1, padx=3, pady=2)
        self.com = Combobox(self.top, value=[i for i in range(1, 8)])
        self.com.grid(row=0, column=2, padx=8, pady=2, ipadx=50)
        self.entry, button = f.loop_one(f, Data.Amount_details_entry, self.top)
        self.com.bind('<<ComboboxSelected>>', lambda x: self.change_data(self.com.get()))
        button.configure(command=self.save_data)
        self.top.mainloop()

    def change_data(self, value):
        data=self.obj.fetchData(data_for_search={'semester':value})
        [i.delete(0,100000) for i in self.entry]
        [i.insert(0,data[0][k+1]) for k,i in enumerate(self.entry[:-1])]

    def save_data(self):

        p=[f'{i}' for i in Data.Amount_details_entry]
        l={p[q]:f'"{i.get()}"' for q,i in enumerate(self.entry[:-1])}

        self.obj.update(l,{'semester':self.com.get()})
        self.top.destroy()
