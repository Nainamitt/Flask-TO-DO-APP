# pending , working , done------main ki table bnata hai yeh 

# yha db jo init mai bna hai woh import hora hai yha pai
from app import db

class Task(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(100) , nullable = False)
    status = db.Column(db.String(20) , default = "Pending")
    