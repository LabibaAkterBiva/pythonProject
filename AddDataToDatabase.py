import firebase_admin

from firebase_admin import credentials

from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendence-e2099-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "2003154":
        {
            "name": "Elon Musk",
            "major": "CEO of SpaceX",
            "starting_year": 2023,
            "total_attendance": 3,
            "year": 1,
            "last_attendance_time": "2023-03-11 00:54:34"
        },
    "2003155":
        {
            "name": "Bil Gates",
            "major": "American Buisness Magnate,investor",
            "starting_year": 2023,
            "total_attendance": 4,
            "year": 1,
            "last_attendance_time": "2022-03-11 00:54:34"
        },
    "2003156":
        {
            "name": "Labiba Akter Biva",
            "major": "CSE student",
            "starting_year": 2023,
            "total_attendance": 5,
            "year": 1,
            "last_attendance_time": "2022-03-11 00:54:34"
        }
}
for key, value in data.items():
    ref.child(key).set(value)