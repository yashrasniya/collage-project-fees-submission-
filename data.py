from tkinter import *
from datetime import datetime
from tkcalendar import DateEntry
from tkinter.ttk import *
import sqlite3
# from ttkbootstrap import *
# from ttkbootstrap.style import Style
# from ttkbootstrap.constants import *
from data_base.data_base_conecter import Database


class Data:
    branch = [
        'Computer Science Engineering',
        'Mechanical Engineering',
        'Electronics & Communication',
        'Electronics Engineering',
        'Civil Engineering'
    ]

    Batch = [f"{a}-{a + 4}" for a in range(2014, 1 + int(str(datetime.now()).split("-")[0]))]

    NONE = 'Select an Option'
    option = {}
    _grid = {'ipadx':50}
    Entry_name_New_Student = {
        'Name': {'widget': Entry, 'value': None, 'option': option, 'grid': _grid},
        'Father Name': {'widget': Entry, 'value': None, 'option': option, 'grid': _grid},
        'Batch': {'widget': Combobox, 'value': Batch, 'option': {'state':'readonly'}, 'grid': {'ipadx':40}},
        'Branch': {'widget': Combobox, 'value': branch, 'option': {'state':'readonly'}, 'grid': {'ipadx':40}},
        'Mobile Number': {'widget': Spinbox, 'value': None, 'option': option, 'grid': {'ipadx':38}},
        'Email ID': {'widget': Entry, 'value': None, 'option': option, 'grid': _grid},
        'Roll Number': {'widget': Spinbox, 'value': None, 'option': option, 'grid': {'ipadx':38}},

    }

    Semester = [
        f'{a}-Semester' for a in range(1, 9)
    ]
    Entry_name_Fees_Submission = {
        'Date': {'widget': DateEntry, 'value': None, 'option': option, 'grid': _grid},
        'Receipt Number': {'widget': Entry, 'value': None, 'option': option, 'grid': _grid},
        'Transaction Number': {'widget': Entry, 'value': None, 'option': option, 'grid': _grid},
        'Semester': {'widget': Combobox, 'value': Semester, 'option': option, 'grid': {'ipadx':40}},
        'Amount': {'widget': Button, 'value': None, 'option': option, 'grid': {'ipadx':80}},

    }

    grid_data = {
        'padx': 3, 'pady': 2
    }

    grid = {'row': 0, 'column': 2}
    frames_three_entrys_data = {
        'Batch': [[Combobox, Combobox], grid, [{'Branch': [Combobox, {}, branch],
                                                'Date': [DateEntry, {}, None],
                                                'Name': [Entry, {}, None],
                                                'Semester': [Combobox, {}, Semester]
                                                }, Batch],
                  ],
        'Receipt Number': [[Entry], grid, None],
        'Date': [[DateEntry, DateEntry], grid, None],
        'Transaction Number': [[Entry], grid, None],
        'Roll Number': [[Spinbox], grid, None],
        'Mobile Number': [[Spinbox], grid, None],
        'All': [[], grid, None]

    }
    frames_three_Combobox_propertys = {
        'width': 15,
    }
    NSD = 'New_Student14'
    FS = 'Fees_Submission111'
    rollNumber = "Roll Number"
    showing_elements = ['[Name]', f'[{NSD}].[{rollNumber}]', '[Father Name]']
    showing_elements_forDisplay = {'Name', rollNumber, 'Father Name'}
    showing_elements_forDisplay_array = ['Name', rollNumber, 'Father Name']
    showing_elements_on_box = ['[Name]',
                               '[Father Name]',
                               '[Batch]',
                               '[Branch]',
                               "[Mobile Number]",
                               '[Email ID]',
                               f'[{NSD}].[{rollNumber}]'
                               '[Date]', '[Receipt Number]',
                               '[Transaction Number]', 'Semester', 'Amount',
                               '[Tuition Fee]',
                               ' [Exam Fee]',
                               ' [Enrollment fee] ',
                               ' [Registration Fee] ',
                               ' [Security Deposited]',
                               ' [Sport Fee] ',
                               ' [Development Fee] ',
                               ' [Welfare Fee] ',
                               '[Dues]']
    con = sqlite3.connect("database.db")
    obj = Database(con)

    # menu bar
    menu = {
        'File': {
            'new': None,

        },
        'options': {
            'Email': None,
            'sms': None,
            'default value': None
        },

    }
    # Amount detail
    g = {'ipadx':50}
    o = {}
    Tdsn = 25  # temp data saver number
    Amount_detail_table = 'Amount_detail'
    Amount_details_entry = {
        'Tuition Fee': {'widget': Entry, 'value': None, 'option': o, 'grid': g},
        'Exam Fee': {'widget': Entry, 'value': None, 'option': o, 'grid': g},
        'Enrollment fee': {'widget': Entry, 'value': None, 'option': o, 'grid': g},
        'Registration Fee': {'widget': Entry, 'value': None, 'option': o, 'grid': g},
        'Security Deposited': {'widget': Entry, 'value': None, 'option': o, 'grid': g},
        'Sport Fee': {'widget': Entry, 'value': None, 'option': o, 'grid': g},
        'Development Fee': {'widget': Entry, 'value': None, 'option': o, 'grid': g},
            'Welfare Fee': {'widget': Entry, 'value': None, 'option': o, 'grid': g},
        'Amount': {'widget': Entry, 'value': None, 'option': {'state':DISABLED}, 'grid': g},

    }

    # email detail
    email_detail = {
        'port': 465,
        'smtp_server': "smtp.gmail.com",
        'sender_email': "yashrsniya@gmail.com",
        'receiver_email': "yashrasniya3@gmail.com",
        'password': 'YasH*8938#',
        'message': '''
        Subject:hello
        
        Hello
        '''
    }
# DateEntry(win, width= 16, background= "magenta3", foreground= "white",bd=2)
