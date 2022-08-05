from data import Data as D


class Config:
    # new student create table detali
    NSCTD = '''Name TEXT NOT NULL , 
            [Father Name] TEXT NOT NULL , 
            Batch TEXT NOT NULL ,
            Branch TEXT NOT NULL ,
            [Mobile Number] INTEGER NOT NULL ,
            [Email ID] TEXT NOT NULL ,
            [Roll Number] INTEGER NOT NULL PRIMARY KEY
            '''
    # fess Submission detail

    FSD = '''
    ID INTEGER  PRIMARY KEY ,
    [Roll Number] INTEGER ,
    Date_real TEXT,
    Date TEXT,
    [Receipt Number] TEXT,
    [Transaction Number] TEXT,
    Semester TEXT,
    Amount INTEGER,
    [Tuition Fee] TEXT,
    [Exam Fee] TEXT,
    [Enrollment fee] TEXT,
    [Registration Fee] TEXT,
    [Security Deposited] TEXT,
    [Sport Fee] TEXT,
    [Development Fee] TEXT,
    [Welfare Fee] TEXT,
    [Dues] BLOB
    '''
    col_name = '''(Name  , 
            Father ,
            Batch ,
            Branch, 
            Mobile ,
            EmailID,
            Roll )
            '''
    data_types = {
        D.NSD: [NSCTD],
        D.FS: [FSD]
    }
    ELCT = 'ELCT'
    Email_login_data = '''
    id INTEGER NOT NULL PRIMARY KEY ,
    Email TEXT,
    Password TEXT
    '''
    # Amount detail database collum name
    ADDBCN = '''
        semester INTEGER NOT NULL  PRIMARY KEY ,
            [Tuition Fee] TEXT,
            [Exam Fee] TEXT,
            [Enrollment fee] TEXT,
            [Registration Fee] TEXT,
            [Security Deposited] TEXT,
            [Sport Fee] TEXT,
            [Development Fee] TEXT,
            [Welfare Fee] TEXT
        '''