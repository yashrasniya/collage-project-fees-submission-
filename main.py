from Frame.frame import *
import tkinter as tk
import tkinter.ttk as ttk
import time
import autoThings
# import ttkbootstrap as ttk
# from ttkbootstrap.constants import *
# from ttkbootstrap.style import Style
from menu_bar.menuBar import _Menu_Bar

class Main(Frame):
    def __init__(self, root):
        super().__init__()
        self.root = root

        _Menu_Bar(root)
        # root.resizable(False, False)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        # s=tk.ttk.Style()
        # print(s.theme_names())
        # s.theme_use('yeti')
        # #######################################
        # style = Style()
        # style = Style(theme='superhero')

        # ttk.Window('xx','darkly')
        #########################################
        # s.theme_use('default')
        # a='''C:\\Users\\Yash\\Downloads\\awthemes-10.4.0\\awthemes-10.4.0'''
        # root.tk.call('lappend', 'auto_path', a)
        # root.tk.call('package', 'require', 'awdark')
        self.can = Canvas(root, height=550, width=1000)
        # self.r = ttk.Notebook(self.root)
        self.r = ttk.Frame(self.root)
        # self.r.pack(expand=1,fill=BOTH)
        self.can.pack(side=TOP,anchor='nw')
        self.can.create_window((2, 2), window=self.r, anchor='nw')
        self.geometry_properties()
        self.frame_3()
        self.Frame_1()
        # Label(self.root,text="hello").pack()
        self.Frame_2()
        # sg = ttk.Sizegrip(root)
        # sg.grid(row=1, sticky=tk.SE)


    def geometry_properties(self):
        self.root.geometry('1000x600')
        self.root.title('collage project')


if __name__ == '__main__':
    root = Tk()
    a = Main(root)
    root.mainloop()
