from tkinter import *
from tkinter.ttk import *
from Frame.frameCommanThings import FrameCommonThings
from tkinter.messagebox import *
from tkcalendar import DateEntry
from Frame.toplavel_frame import *


class FrameSecond(FrameCommonThings):
    amount_data=[]
    def Frame_2(self):
        can = Canvas(self.r, height=200, width=50)
        # self.r.add(can,text='Fees Submission')
        can.pack(side=TOP, anchor='w')
        frame = LabelFrame(
            can,
            text='Fees Submission'
        )
        can.create_window((0, 0), window=frame, anchor='nw')
        frame.grid(row=1, column=0)
        frame_Entry_element = LabelFrame(frame)
        frame_Entry_element.grid(row=1, column=0)
        # frame_Entry_element['state']=DISABLED
        self.search_student_layout(frame, frame_Entry_element)

    def search_student_layout(self, frame, frame_Entry_element):
        root = LabelFrame(
            frame,
            text='Search Student'
        )

        root.grid(row=0, column=0, columnspan=5)

        Label(root, text='Roll Number').grid(row=0, column=0, **self.grid_data)
        RollNumber = Entry(root)

        RollNumber.grid(row=0, column=1, **self.grid_data)
        self.list, self.save_button = self.loop_one(self.Entry_name_Fees_Submission, frame_Entry_element)
        self.change_state(DISABLED)
        # amount button config
        self.list[-1].bind('<Control-Key-p>', lambda a:AmountDetail(frame_Entry_element,self.list))
        self.list[-1]['command']=(lambda :AmountDetail(frame_Entry_element,self.list))
        self.list[-1]['text']='0.0'
        ##################################################################################
        self.save_button['state'] = DISABLED
        bu = Button(root, text="Search", command=lambda: self.Search(root, RollNumber, bu, frame_Entry_element))
        bu.grid(row=0, column=2, **self.grid_data)
        RollNumber.bind('<Return>', lambda a: self.Search(root, RollNumber, bu, frame_Entry_element))

    def change_state(self, state_type):
        for i in self.list:
            if (type(i)==Combobox or type(i)==DateEntry) and state_type=='normal':
                i['state']='readonly'
            else:
                i.configure(state=state_type)
                i['state'] = state_type

    def Search(self, r, Entry_obj, button_obj, frame_Entry_element):
        try:
            roll_number = int(Entry_obj.get())
        except ValueError as e:
            showerror('error', 'INTEGER Plz')
            return
        self.obj.table = self.NSD
        r_cl = self.obj.fetchData(only_this=f"[{self.rollNumber}]")  # roll number check list
        if (roll_number,) in r_cl:
            self.list[-1].bind('<Return>', (lambda x: self.Save(self.list, RollNumber=roll_number)))
            self.save_button['command'] = lambda: self.Save(self.list, RollNumber=roll_number)
            root = LabelFrame(r, width=300, height=40)
            root.propagate(0)
            root.grid(row=1, column=0, **self.grid_data, columnspan=3)
            self.change_state('normal')
            self.save_button['state'] = NORMAL
            for i in self.obj.fetchData(data_for_search={self.rollNumber: roll_number})[0][:4]:
                Label(root, text=i).pack(side=LEFT, anchor='nw')
            Entry_obj['state'] = DISABLED
            button_obj['text'] = 'X'
            button_obj['command'] = lambda: self.DeSearch(root, Entry_obj, button_obj, r, frame_Entry_element)
        else:
            showerror('error', 'Check roll number again....')

    def DeSearch(self, root, Entry_obj, button_obj, r, f):
        self.change_state(DISABLED)
        root.grid_forget()
        Entry_obj['state'] = NORMAL
        button_obj['text'] = 'Search'
        self.save_button['state'] = DISABLED
        button_obj['command'] = lambda: self.Search(r, Entry_obj, button_obj, f)
