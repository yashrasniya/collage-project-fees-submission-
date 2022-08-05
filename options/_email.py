import smtplib, ssl
from data import Data as d
from tkinter.ttk import *
from tkinter import *
from data_base.database_config import Config
from tkinter.messagebox import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import webbrowser

url='https://myaccount.google.com/lesssecureapps'
# https://realpython.com/python-send-email/
def EmailSending(email, password, sender_email, subject, text=None, html=None):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = email
    message["To"] = sender_email
    if text:
        part1 = MIMEText(text, "plain")
        message.attach(part1)
    if html:
        part2 = MIMEText(html, "html")
        message.attach(part2)

    context = ssl.create_default_context()
    # showwarning('error', 'code is commented')
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(email, password)
            server.sendmail(
                sender_email, sender_email, message.as_string()
            )
            showinfo('Done', 'mail was sent....')
    except smtplib.SMTPRecipientsRefused as e:
        showwarning('error', e)


def student_fees_submission_confection(**kwargs):
    d.obj.table = d.NSD
    i = {'Roll Number': kwargs['Roll Number']}
    auth = d.obj.fetchData(data_for_search=i)[0]
    d.obj.table = d.Amount_detail_table
    p = {'semester': kwargs['semester'][0]}

    default = d.obj.fetchData(data_for_search=p)[0]
    d.obj.table = d.FS
    # Total submit Fess Array
    TSFA = d.obj.fetchData(data_for_search={'Roll Number': kwargs['Roll Number']
        ,
                                            'Semester': f"'{kwargs['semester']}'"
                                            }, only_this='Amount')
    default_sum = 0
    TSF = 0  # Total submit Fess
    for i in TSFA:
        try:
            TSF += int(i[0])
            print(i)
        except ValueError as e:
            print(e)

    for i in default[1:]:
        try:
            default_sum += int(i)
        except ValueError as e:
            print(e)
    print(default_sum, TSFA,TSF)
    email = auth[5]

    done = f'{auth[0]},your fees is Submitted..'
    due=''
    if default_sum > TSF:

        due=f'and your due is {default_sum - TSF}'

    other = f'''you submit {kwargs["amount"]} {due},your Receipt Number is {kwargs[
        "Receipt Number"]}'''
    email_confection(data=[done, other], email=email)


def email_confection(data, email):
    d.obj.table = Config.ELCT
    i = {'id': 1}
    auth = d.obj.fetchData(data_for_search=i)

    with open('layout/html/student_detail.html', 'r') as r:
        re = r.read()
        k = re.split('{{}}')
        file = ''
        for j, i in enumerate(k):
            print(j)
            file += i
            if len(k) - 1 != j:
                file += data[j]
        EmailSending(auth[0][1], auth[0][2], email, html=file, subject='submitted')


def save_EP(e1, e2):
    d.obj.table = Config.ELCT

    da = {'Email': f'"{e1.get()}"', 'Password': f'"{e2.get()}"'}
    i = {'id': 1}
    d.obj.update(da, i)
    showinfo("Done", 'Email-Password are saved')
    e1.delete(0, 1000000000)
    e2.delete(0, 1000000000)


class email_data_changer:
    def __init__(self, root):
        self.top = Toplevel(root)
        ####################
        self.text_frame=Frame(self.top)
        self.text_frame.pack()
        Label(self.text_frame,text='Make sure you turn off the two facter authentication \
        \n in google account if not click link below').pack()
        link=Label(self.text_frame,text='google',fg='blue')
        link.pack()
        link.bind('<Button-1>',lambda e: webbrowser.open_new_tab(url))
        ####################
        self.main_frame=Frame(self.top)
        self.main_frame.pack()

        self.grid = {}
        Label(self.main_frame, text='Email').grid(row=0, column=0, **self.grid)
        Label(self.main_frame, text='password').grid(row=1, column=0, **self.grid)

        e1 = Entry(self.main_frame)
        e1.grid(row=0, column=1, **self.grid)
        e2 = Entry(self.main_frame)
        e2.grid(row=1, column=1, **self.grid)

        b = Button(self.main_frame, text='save', command=lambda: save_EP(e1, e2))
        b.grid(row=3, column=0, )
        b2 = Button(self.main_frame, text='Check', command=lambda: self.checking(e1.get(), e2.get(), b2))
        b2.grid(row=3, column=1)
        self.main_frame.mainloop()

    def checking(self, email, password, b):
        Label(self.main_frame, text='To').grid(row=2, column=0, **self.grid)
        sE = Entry(self.main_frame)
        sE.grid(row=2, column=1)
        b.configure(text='send', command=lambda: EmailSending(email, password, sE.get(), 'checking'))


if __name__ == '__main__':
    root=Tk()
    email_data_changer(root)
    root.mainloop()
