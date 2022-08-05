import firebase_admin
# from firebase_admin import credentials
import time
from firebase_admin import firestore
from data import Data as D

default_app = firebase_admin.credentials.Certificate('C:\\Users\\Yash\\collage projaect\\Certificate.json')
default_app = firebase_admin.initialize_app(default_app, {
    'databaseURL': 'https://collage-project-for-fees-default-rtdb.firebaseio.com/'
})

obj = firestore.client()


class FireConnect:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def create_collection(self):
        data = ''
        if self.name == D.NSD:
            data = {
                'Name': self.data[0],
                'Father Name': self.data[1],
                'Batch': self.data[2],
                'Branch': self.data[3],
                'Mobile Number': self.data[4],
                'Email ID': self.data[5],
                'Roll Number': self.data[6]
            }
        if self.name == D.FS:
            data = {
                'Date': self.data[0],
                'Receipt Number': self.data[1],
                'Transaction Number': self.data[2],
                'Semester': self.data[3],
                'Amount': self.data[4],
                'Date_real': time.time(),

            }
        k = obj.collection(self.name).add(data)
        return k

    def update_collection(self, rollnumber):
        data = ''
        obj.collection(self.name).add(data)

    def get_data(self, L):
        k = obj.collection(self.name).document(L)
        return k.get()


if __name__ == '__main__':
    f = FireConnect('rollNumber', [
        'ram', 'naveen', '30303', 'dsf', 8938095294, 'yashrasniya3@gmail.com', 1
    ])
    k = f.get_data('1')
    print(type(k))
