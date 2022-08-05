from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import *
from Frame.frameCommanThings import FrameCommonThings
from data_base.database_manager import *
from Frame.toplavel_frame import ShowingData


class FrameEntry:
    entry_frame = []
    a = []
    c = ''

    def frame_entry_maker(self, label_frame, extra_data, *args, **kwargs):
        self.a.clear()
        self.entry_frame.append(Frame(label_frame))
        self.entry_frame[-1].grid(**kwargs)

        for j, i in enumerate(args):
            if extra_data:
                self.a.append(i(self.entry_frame[-1], value=[j for j in extra_data[j]]))
                if type(extra_data[j]) is dict:
                    self.a[-1].bind('<<ComboboxSelected>>',
                                    lambda e, d=j, k=self.a[-1]: self.make(self.entry_frame[-1],
                                                                           extra_data[d].get(k.get())))
            else:
                self.c = ''
                self.a.append(i(self.entry_frame[-1]))
            self.a[-1].pack(side=LEFT)

    def make(self, master, DList):
        if self.c != '':
            self.a.remove(self.c)
            self.c.pack_forget()
        if DList[2]:
            self.c = DList[0](master, value=DList[2], **DList[1])
            self.c.pack(side=LEFT)
        else:
            self.c = DList[0](master, **DList[1])
            self.c.pack(side=LEFT)
        self.a.append(self.c)


class FrameThird(FrameCommonThings, FrameEntry):
    showed_data = []

    def frame_3(self):
        can = Canvas(self.r, height=200, width=50)

        can.pack(side=RIGHT)
        frame = LabelFrame(
            can,
            text='list',width=500
        )
        frame.propagate(0)
        frame.grid(row=0, column=1, rowspan=2)
        can = Canvas(frame, height=400, width=300, border=0)

        list_frame = Frame(frame,width=700,height=400)
        list_frame.propagate(0)
        list_frame.grid(row=1, column=0, columnspan=10, padx=0)
        # ============================================================================================
        # Header layout
        # =============================================================================================
        l = Label(frame, text='Choice')
        l.grid(row=0, column=0)
        b = Button(frame, text='Show')
        b.grid(row=0, column=3)
        combobox = Combobox(frame, value=[i for i, k in self.frames_three_entrys_data.items()],
                            **self.frames_three_Combobox_propertys)

        combobox.grid(row=0, column=1, **self.grid_data)
        combobox.set(self.NONE)

        combobox.bind('<<ComboboxSelected>>',
                      lambda x: self.callback(self.frames_three_entrys_data, frame, data=combobox.get()))
        tree = Treeview(list_frame, columns=D.showing_elements_forDisplay_array, show='headings', height=20, padding=0,
                        selectmode='browse')
        tree.pack()
        [tree.column(f'# {i + 1}', stretch=NO, anchor=CENTER, width=700) for i, j in
         enumerate(D.showing_elements_forDisplay_array)]
        b['command'] = lambda: self.do(tree, combobox, *self.a)
        # ===========================================================================================

        scrollbar = Scrollbar(frame, orient="vertical", command=can.yview)
        can.config(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=1, column=7, sticky='NSW')
        can.create_window((0, 0), window=list_frame, anchor="nw")
        list_frame.grid(row=1, column=0, columnspan=5, padx=0)
        list_frame.bind(
            "<Configure>",
            lambda e, can=can: can.configure(
                scrollregion=can.bbox("all")
            )
        )

        # can.grid(row=1, column=0, columnspan=5,padx=0)

    def item_selected(self, tree, f):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            ShowingData(f, record[1])

    def do(self, tree, *args, **kwargs):

        [tree.delete(i) for i in tree.get_children()]
        k = Organizing([i.get() for i in args])
        j = k.return_array
        if not j:
            return
        else:

            self.showed_data = set(j)
            copy_list=[]
            copy_list=D.showing_elements_forDisplay_array.copy()
            copy_list.append(k.type)
            copy_list=list(dict.fromkeys(copy_list))
            tree['columns'] = copy_list

            [tree.heading(i, text=i) for i in copy_list]
            [tree.column(f'# {i + 1}', stretch=NO, anchor=CENTER, width=100) for i, j in
             enumerate(copy_list)]

            array = D.showing_elements

            tree.bind('<<TreeviewSelect>>', lambda e: self.item_selected(tree, tree))
            n = 0
            j = set(j)
            for i in j:


                frame = Frame(tree)
                # frame.pack()
                d = [f'{l}' for p, l in enumerate(i)]
                tree.insert('', 0, value=d)
                Button(frame, text=f'{i[1]}-{i[0]},{i[2]}', command=lambda f=frame, d=i[1]:
                (ShowingData(f, d))).grid(row=0, column=n, ipadx=100)
                n += 1

    def callback(self, values, master, *args, **kwargs):
        if self.entry_frame:
            self.entry_frame[-1].grid_forget()
        data = kwargs['data']
        new_list = values[data]
        self.frame_entry_maker(master, new_list[2], *new_list[0], **new_list[1])
