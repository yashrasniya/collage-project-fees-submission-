from options._email import *
from data_base.database_config import Config
from data import Data as D


class DatabaseManager(Config):
    def __init__(self, data_type, array, **kwargs):
        if kwargs:
            self.RollNumber = kwargs['RollNumber']
        self.array = array
        self.obj = D.obj
        self.obj.table = data_type
        self.database_con_config = self.data_types[self.obj.table]
        self.obj.creatingTable(self.database_con_config[0])  # creating new table for new student
        if data_type == D.NSD:
            self.ForNewS()
        if data_type == D.FS:
            self.ForFeeSubmission()
        self.obj.fetchData(print_data=True)

    def ForNewS(self):

        self.obj.IE(
            f'''( "{self.array[0]}" , 
                    "{self.array[1]}" , 
                    "{self.array[2]}" , 
                    "{self.array[3]}" , 
                    {self.array[4]} , 
                    "{self.array[5]}" , 
                    {self.array[6]}  )''')

    def getting_data_from_temp_location(self, t, d):
        temp = self.obj.table
        b = False
        self.obj.table = t
        data = self.obj.fetchData(data_for_search=d)
        d['semester'] = self.array[3]
        check_data = self.obj.fetchData(data_for_search=d)
        self.obj.table = temp
        temp_value = 0
        for i in check_data:
            try:
                temp_value += int(i)
            except TypeError as e:
                print(e)
        data = [f"'{i}'" for i in data[0][1:]]
        data.append(str(temp_value >= self.array[4]))
        return ' , '.join(data)

    def ForFeeSubmission(self):
        dd = self.getting_data_from_temp_location(D.Amount_detail_table, {'semester': D.Tdsn})
        print(dd)
        if dd[0] is 'None':
            print("dd")
            return
        self.obj.IE(
            f'''( NULL , 
                            {self.RollNumber},
                            datetime('now'),
                            '{self.array[0]}',
                            "{self.array[1]}" , 
                            "{self.array[2]}" , 
                            "{self.array[3]}" , 
                            {self.array[4]} , 
                             {dd} )''')
        p = [f'{i}' for i in D.Amount_details_entry]
        l = {p[q]: f'"{None}"' for q, i in enumerate(p)}

        self.obj.update(l, {'semester': D.Tdsn})
        student_fees_submission_confection(**{'Receipt Number': self.array[1],
                                           'Roll Number': self.RollNumber,
                                           'semester': self.array[3],
                                           'amount': self.array[4]})


class Organizing:
    def __init__(self, ty_ele_array, *args, **kwargs):
        self.elements = ty_ele_array[1:]
        self.type = ty_ele_array[0]
        self.return_array = []
        self.obj = D.obj  # connect to database
        self.obj.table = D.NSD
        self.showing_elements = D.showing_elements.copy()
        if not self.type in ['Roll Number', 'Name', 'All']:
            self.showing_elements.append(f"[{self.type}]")
        if self.type == 'Batch':
            self.Batch()

        elif self.type == 'Receipt Number':
            self.collector({self.type: f'"{self.elements[0]}"'})

        elif self.type == 'Date':
            self.Date()

        elif self.type == 'Roll Number':
            self.collector({self.type: self.elements[0]})
        elif self.type == 'Transaction Number':
            self.collector({self.type: self.elements[0]})
        elif self.type == 'Mobile Number':
            self.collector({f'{self.type}': f"{self.elements[0]}"})
        elif self.type == 'All':
            self.return_array.extend(self.obj.join_table(','.join(self.showing_elements)))

    def collector(self, dis, join_type=None):
        if join_type:
            self.return_array.extend(self.obj.join_table(','.join(self.showing_elements),
                                                         where=dis, join_type=join_type))
            return
        self.return_array.extend(self.obj.join_table(','.join(self.showing_elements),
                                                     where=dis))

    def Batch(self):

        type_e = self.elements[0]
        elements = self.elements[1:]
        self.collector({self.type: f'"{elements[0]}"', type_e: f'"{elements[1]}"'})

    def Date(self):
        self.return_array.extend(self.obj.join_table(','.join(self.showing_elements),
                                                     beetween=[f'"{self.elements[0]}"', f'"{self.elements[1]}"'],
                                                     col_name=f'{self.type}'))


def all_data_by_roll_number(r):
    obj = D.obj  # connect to database
    obj.table = D.NSD
    return obj.join_table(' , '.join(D.showing_elements_on_box), where={D.rollNumber: r})


def update_items(d, i, table):  # d= data,i =id
    obj = D.obj
    obj.table = table
    obj.update(d, i)
    return obj.fetchData()
