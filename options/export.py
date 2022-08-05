import gspread
from datetime import datetime

account = gspread.service_account()


def exporter(file_name, _data, location, worksheet_name=None, email_id=None, file_ex=True, *args, **kwargs):
    if file_ex:
        sheet = account.open(file_name)
        if worksheet_name:
            _worksheet = sheet.worksheet(worksheet_name)
        else:
            _worksheet = sheet.add_worksheet(str(datetime.now() ), rows=1000, cols=20)
    else:
        sheet = account.create(file_name)
        if email_id:
            sheet.share(email_id, perm_type='user', role='writer')
        _worksheet = sheet.add_worksheet(str(datetime.now()), rows=1000, cols=20)
    _worksheet.update(location, _data)

def assembler(data,email=None):
    array=data
    for i in array:
        if type(i)== list:

if __name__ == "__main__":
    data = [[2, 4], [56, 64]]
    location = 'A1:B2'
    exporter('test_1', data, location, email_id='yashrasniya3@gmail.com', file_ex=False)
