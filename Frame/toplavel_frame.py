from tkinter import *
from tkinter.ttk import *
from Frame.frameCommanThings import FrameCommonThings
from data_base.database_manager import *
from data import Data
from tkinter.messagebox import *
from Log.log import *


class ShowingData:
    frame_list = ''

    def __init__(self, f, d):
        self.make_detail(f, d)
        # if self.frame_list != '':
        #     self.frame_lis

    def make_detail(self, f, d):
        all = all_data_by_roll_number(d)
        print(all)
        common_data, other_data = all[0][:7], [i[6:] for i in all]
        # f.grab_set()
        top = Toplevel(f)
        self.frame_list = top
        l = LabelFrame(top, text=d)
        l.pack(expand=1, fill=X)
        tree = Treeview(l, columns=D.showing_elements_on_box[6:], show='headings')
        [tree.column(f'# {i + 1}', stretch=NO, anchor=CENTER, width=100) for i, j in
         enumerate(D.showing_elements_on_box[7:])]
        [tree.heading(i, text=i) for i in D.showing_elements_on_box[7:]]

        f = Frame(l)
        f.pack(side=TOP)
        tree.pack(side=TOP)
        f1 = Frame(f)
        f1.pack(side=LEFT)
        f2 = Frame(f)
        f2.pack(side=LEFT)
        print(other_data)
        if other_data[0][1] and other_data[0][2] and other_data[0][3]:
            self.SVI(f2, [i[4] for i in other_data], [i[3][0] for i in other_data], [i[-1] for i in other_data])
        entry_list, save_button = FrameCommonThings.loop_one(FrameCommonThings(), Data.Entry_name_New_Student, f1)
        for i, j in enumerate(entry_list):
            j.delete(0, 10000000)
            j.insert(0, common_data[i])
            j.configure(state=DISABLED)
        save_button.configure(text="Edit", command=lambda: self.edit(entry_list, save_button))
        for i, j in enumerate(other_data):
            d = [f'{l}' for p, l in enumerate(j)]
            tree.insert('', 0, value=d)
        top.mainloop()

    def edit(self, e_list, button):
        button.configure(text='Save', command=lambda: self.updates(e_list, button))
        for i, j in enumerate(e_list[:-1]):
            if type(j) == Combobox:
                j.configure(state='readonly')
            else:
                j.configure(state='normal')

    def SVI(self, f, a, s, dues_b):  # f= frame,a=amount,s=semester //some value information
        obj = Data.obj
        s_copy = set(s.copy())
        obj.table = Data.Amount_detail_table
        main_amount = {i: obj.fetchData(data_for_search={'semester': i})[0][1:] for i in s_copy}
        amount = {i: 0 for i in s_copy}
        for i in main_amount:
            temp = 0
            for l in main_amount[i]:
                wr(l)
                try:
                    temp = int(l) + temp
                except ValueError as e:
                    wr(e)
            main_amount[i] = temp
        for i, j in enumerate(s):
            amount[j] += a[i]

        for i in main_amount:
            if main_amount[i] > amount[i]:
                main_amount[i] = main_amount[i] - amount[i]
            else:
                main_amount[i] = main_amount[i] - amount[i]
        total_due = 0
        for i in main_amount:
            total_due += main_amount[i]
            Label(f, text=f'{i} semester: {main_amount[i]}').pack()
        Label(f, text=f'total due is  {total_due}').pack()

    def updates(self, e, b):  # entry class list
        l = [i.get() for i in e]
        o = [i for i in Data.Entry_name_New_Student]
        f = {o[i]: f'"{p}"' for i, p in enumerate(l[:-1])}
        f['Mobile Number'] = int(f['Mobile Number'][1:-1])
        id = {o[-1]: l[-1]}
        update_items(f, id, Data.NSD)
        b.configure(text="Edit",
                    command=lambda:
                    self.edit(e, b))
        for i in e:
            i['state'] = DISABLED


class AmountDetail:
    def __init__(self, frame, main_entry):
        self.finely = []
        self.main_entry = main_entry
        self.obj = Data.obj
        self.obj.table = Data.Amount_detail_table
        if main_entry[-2].get() == '' or main_entry[-2].get() == Data.NONE:
            showwarning('warning', 'fill semester......')
            return
        self.top = Toplevel(frame)
        self.entry, button = FrameCommonThings.loop_one(FrameCommonThings(), Data.Amount_details_entry, self.top)
        button.configure(command=self.SAD)
        sem = main_entry[-2].get()[0]
        self.fill_data(sem)
        self.APTE()
        self.top.mainloop()

    def APTE(self):  # adding properties to entry
        for i, j in enumerate(self.entry[:-1]):
            j.bind('<Button-1>', self.callback)
            j.bind('<Tab>', self.callback)

    def callback(self, e):
        a = 0
        for i, j in enumerate(self.entry[:-1]):
            print(j.get())
            try:
                a += int(j.get())
            except ValueError as e:
                wr(e, 'callback at amount box!')
        self.entry[-1]['state'] = 'normal'
        self.entry[-1].delete(0, 10000000)
        self.entry[-1].insert(0, a)
        self.entry[-1]['state'] = 'readonly'

    def SAD(self):  # save Amount Detail
        k = 0
        for i in self.entry[:-1]:
            if i.get() == '':
                self.finely.append(None)
            else:
                self.finely.append(i.get())

                try:
                    k += int(i.get())
                except ValueError as e:
                    wr(e)
        self.finely = [f"'{i.get()}'" for i in self.entry[:-1]]
        self.main_entry[-1]['text'] = k
        self.main_entry[-2]['state'] = 'readonly'

        p = [f'{i}' for i in Data.Amount_details_entry]
        l = {p[q]: f'{i}' for q, i in enumerate(self.finely)}

        self.obj.update(l, {'semester': Data.Tdsn})
        self.top.destroy()

    def fill_data(self, sem):

        data = self.obj.fetchData(data_for_search={'Semester': sem})
        [self.entry[i].insert(0, j) for i, j in enumerate(data[0][1:])]
