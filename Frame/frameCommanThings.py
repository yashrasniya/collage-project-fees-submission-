from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import pyperclip as pc
from Log.log import *

import data
from data_base.database_manager import DatabaseManager


class FrameCommonThings(data.Data):
    def Save(self, l, **kwargs):

        b = 1
        array = []

        for j, i in enumerate(l):
            if type(i) != Button:

                if i.get().upper() != 'SELECT AN OPTION' and i.get().upper() != '':
                    if type(i) == Spinbox:
                        try:
                            array.append(int(i.get()))
                        except ValueError as e:
                            self.Warning(f'Entry No. {b} is int type!')
                            wr("error", e)
                            return
                    else:
                        array.append(i.get())
                    b += 1
                else:
                    wr('Fill all Entry')
                    self.Warning(f'Entry No. {b} is Empty!')
                    return
            else:
                if i['text'] != '0.0':

                    array.append(int(i['text']))
                else:
                    wr('fill amount')
                    self.Warning(f'Amount is not filled......')
                    return
        if len(array) == 7:
            DatabaseManager(self.NSD, array)
        else:
            DatabaseManager(self.FS, array, **kwargs)

        for i in l:
            if type(i) == Button:
                i['text'] = '0.0'
            elif type(i) == Combobox:
                i.set(self.NONE)

            else:
                i.delete(0, 10000000)
                i.insert(0, '')

    def loop_one(self, list, root):
        new_list_entry = []
        new_list_Label = []
        n = 1
        for i in list:
            k = list[i]
            if k['widget'] == Combobox:

                new_list_entry.append(k['widget'](root, value=k['value'], **k['option']))
                new_list_entry[-1].grid(
                    row=n,
                    column=2,
                    padx=8,
                    pady=2,
                    **k['grid'])

                new_list_entry[-1].set(self.NONE)
            else:

                new_list_entry.append(k['widget'](root, **k['option']))
                print(k, new_list_entry[-1])
                new_list_entry[-1].grid(row=n, column=2, padx=8, pady=2, **k['grid'])
            if k['widget'] == Button:
                new_list_entry[-1]['text'] = i
            v = new_list_entry[-1]

            new_list_entry[-1].bind('<Control-Key-u>', lambda a, n=v: self.ShortKeys(n, n.get().upper()))
            new_list_entry[-1].bind('<Control-Key-l>', lambda a, n=v: self.ShortKeys(n, n.get().lower()))
            new_list_entry[-1].bind('<Control-Key-t>', lambda a, n=v: self.ShortKeys(n, n.get().title()))
            new_list_entry[-1].bind('<Control-Key-C>', lambda a: self.Copy_Past(new_list_entry, 'copy'))
            new_list_entry[-1].bind('<Control-Key-V>', lambda a: self.Copy_Past(new_list_entry, 'paste'))
            new_list_Label.append(Label(root, text=i, anchor="w",width=20))

            new_list_Label[-1].grid(row=n, column=1, padx=3, pady=2)
            n += 1
        new_list_entry[-1].bind('<Return>', (lambda x: self.Save(new_list_entry)))
        Save = Button(root, text='Save', command=lambda: self.Save(new_list_entry))
        Save.grid(row=n, column=1, padx=3, pady=2, columnspan=2, ipadx=100)
        return new_list_entry, Save

    def Warning(self, message):
        showwarning(title='Warning', message=message)

    def ShortKeys(self, a, b):
        a.delete(0, 1000000000)
        a.insert(0, b)

    def Copy_Past(self, list, type):
        if type == 'copy':
            a = ''
            for i in list:
                a += i.get() + '\n'
            pc.copy(a)
        elif type == 'paste':
            b = pc.paste().split('\n')
            if len(b) == 1:
                return
            n = 0
            for a in list:
                a.delete(0, 1000000000)
                try:
                    a.insert(0, b[n])
                except IndexError as a:
                    return
                n += 1
