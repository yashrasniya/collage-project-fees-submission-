import sqlite3
import time
from Log.log import *


# from data_base.database_config import  Config
class Database:
    def __init__(self, s):
        self.s = s
        self.table = ''
        self.r = "Roll Number"

    def OSD(self, dis, add_op=None):  # Organizing SEARCH data
        array = []
        for i in dis:
            if i == self.r:
                array.append(f"{self.table}.[{i}]={dis.get(i)}")
            else:
                array.append(f" [{i}]={dis.get(i)} ")
        if add_op:
            return f' {add_op} '.join(array)
        return ' AND '.join(array)

    def creatingTable(self, cl):

        wr(f'''CREATE TABLE [{self.table}] ({cl})''')
        try:
            self.s.execute(f'''CREATE TABLE [{self.table}] ({cl})''')
        except sqlite3.OperationalError as e:
            wr('table is already exists', e)

        self.close()

    def close(self):
        self.s.commit()
        # self.s.close()

    def IE(self, e):
        """
        inserting data in exiting data table
        :param e: data
        :param t: table

        """
        wr(f"""INSERT INTO {self.table} VALUES{e} """)
        self.s.execute(f"""INSERT INTO [{self.table}] VALUES{e} 
        """)
        # self.s.execute(f"""INSERT INTO {self.table} VALUES{e}""")
        self.close()

    # def IE_array(self,e):
    #
    # wr(f"""INSERT INTO {self.table}{Config.col_name}  VALUES ({'?,'*len(e)}\b)""",e)
    # self.s.execute(f"INSERT INTO {self.table}{Config.col_name} VALUES ({'?,'*len(e)}\b)",e)

    def Do(self, d):
        c = self.s.cursor()
        A = f'SELECT [{d}] FROM {self.table}'
        c.execute(A)
        data = c.fetchall()

    def fetchData(self, data_for_search=None, only_this=None, print_data=False, **kwargs):
        c = self.s.cursor()
        if only_this and data_for_search:
            string = self.OSD(data_for_search)
            B = f'SELECT {only_this} FROM [{self.table}] WHERE {string}'
            c.execute(B)
        else:
            if data_for_search:
                string = self.OSD(data_for_search)
                wr(f"""SELECT * FROM {self.table} WHERE 
                                        {string};""")

                c.execute(f"""SELECT * FROM [{self.table}] WHERE 
                                        {string};""")
            elif only_this:

                A = f'SELECT {only_this} FROM [{self.table}]'
                c.execute(A)
            if only_this == None and data_for_search == None:
                c.execute(f"""
                            SELECT * FROM [{self.table}]
                            """)
        data = c.fetchall()
        self.s.commit()
        if print_data:
            for i in data: wr(i)

        else:
            return data

    def join_table(self, need, join_type=None, STable=None, where=None, beetween=None, col_name=None):
        '''

        :param need:
        Data that you want to display
        :param join_type:
        (INNER) JOIN: Returns records that have matching values in both tables
        LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table
        RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table
        FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table

        :param STable:
        second Table
        :return: data
        '''
        s = ''
        b = ''
        if STable == None:
            STable = 'Fees_Submission111'
        if join_type == None:
            join_type = 'LEFT'
        if where:
            s = f" WHERE {self.OSD(where)}"
        if beetween and col_name:
            b = f'WHERE [{col_name}] BETWEEN {beetween[0]} AND {beetween[1]};'
        c = self.s.cursor()
        k = f'''
                        SELECT {need} FROM [{self.table}] {join_type} JOIN [{STable}] 
                        ON [{self.table}].[{self.r}]={STable}.[{self.r}] {s} {b}
                        '''
        wr(k)
        print(k)

        c.execute(k)

        data = c.fetchall()
        return data

    def between(self, need, col_name, value):
        e = f"""
        SELECT {need} 
        FROM [{self.table}] 
        
        """
        c = self.s.cursor()
        wr(e)
        c.execute(e)

        data = c.fetchall()
        return data

    def delete(self, disData):
        data = disData.popitem()
        self.s.execute(f"""
            DELETE FROM {self.table} WHERE {data[0]}={data[1]}    
            """)
        self.s.commit()

    def update(self, d, i):  # d= data,i =id
        s = self.OSD(d, add_op=',')
        id = self.OSD(i)
        k = f"""
                    UPDATE  {self.table} SET {s}WHERE {id}    
                    """
        wr(k)
        print(k)
        self.s.execute(k)
        self.s.commit()


if __name__ == '__main__':
    con = sqlite3.connect("C:\\Users\\Yash\\collage projaect\\database.db")
    obj = Database(con)
    obj.table = 'Fees_Submission11'
    # obj.creatingTable('''Name TEXT NOT NULL ,
    #             Father Name TEXT NOT NULL ,
    #             Batch TEXT NOT NULL ,
    #             Branch TEXT NOT NULL ,
    #             Mobile Number INTEGER NOT NULL ,
    #             EmailID TEXT NOT NULL ,
    #             Roll_Number INTEGER NOT NULL PRIMARY KEY
    #             ''')
    # obj.IE(f'( "dkfjal" , "kjdsalk" , "2018-2022" , "Computer Science Engineering" , 8934 , "aksdjfak" , 3246  )')
    # g=obj.fetchData(data_for_search={'age' : 1640806081.517568},printData=True)
    # g = obj.fetchData(only_this="*")
    # g = obj.fetchData(data_for_search={'Batch': '"2020-2024"','Name':'"yash"'})
    # g=obj.Do(only_this="Name")
    # obj.delete({'age':1640806081.517568})
    # g = obj.fetchData()
    # a=['Name','Receipt_Number','Date_real','New_Student.Roll_Number']
    g = obj.join_table('*', where={'Roll Number': 1})
    # g = obj.between(' , '.join([f'[Fees_Submission1].[Roll Number]', 'Date']), 'Date', ['"2/28/22"', '"3/2/22"'])
    print(g, obj.table)
