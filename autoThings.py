from data import Data as d
from data_base.database_config import Config
import sqlite3

d.obj.table = Config.ELCT
d.obj.creatingTable(Config.Email_login_data)
try:
    d.obj.IE(f'(1,"","")')
except sqlite3.IntegrityError as e:
    print("error", e)

d.obj.table = d.Amount_detail_table
d.obj.creatingTable(Config.ADDBCN)

try:
    [d.obj.IE(f'({i},"12","","","","","","","")') for i in range(1, 8)]

except sqlite3.IntegrityError as e:
    print("error", e)

try:
    d.obj.IE(f'({d.Tdsn},"","","","","","","","")')

except sqlite3.IntegrityError as e:
    print("error", e)
