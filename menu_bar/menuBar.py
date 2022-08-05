from tkinter import *
from tkinter.ttk import *
from data import Data as d
from options._email import *
from options.amount_detail import *

class _Menu_Bar:
    def __init__(self, root):
        self.d = d.menu
        self.menu = Menu(root)
        self._menu()
        root.config(menu=self.menu)


    def _menu(self):
        m = []
        for i in self.d:
            m.append(Menu(self.menu, tearoff=0))
            self.menu.add_cascade(label=i, menu=m[-1])
            print(i)
            self.d['options']['Email']=lambda :email_data_changer(self.menu)
            self.d['options']['default value']=lambda :AM(self.menu)
            [m[-1].add_cascade(label=k, command=self.d[i][k]) for k in self.d[i]]
