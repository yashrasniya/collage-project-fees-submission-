from tkinter import *
from tkinter.ttk import *
from Frame.frameCommanThings import FrameCommonThings


class FrameOne(FrameCommonThings):

    def Frame_1(self):
        can =Canvas(self.r,height=200,width=50)

        can.create_window((0,0))
        can.pack(side=TOP,anchor='w')
        frame = LabelFrame(
            can,
            text='New Student',height=200,width=100
        )
        frame.propagate(0)
        can.create_window((0, 0), window=frame, anchor='nw')
        frame.pack()
        self.loop_one(self.Entry_name_New_Student, frame)
