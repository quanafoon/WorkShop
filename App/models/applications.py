from App.database import db
from .user import User

class Applications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname =  db.Column(db.String, nullable=False)
    lastname = db.Column(db.String(120), nullable=False)
    dob = db.Column(db.Date)
    email = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    transcript = db.Column(db.String(255))
    resume = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, firstname, lastname, dob, email, phone, transcript, resume, user_id):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.email = email
        self.phone = phone
        self.transcript = transcript
        self.resume = resume
        self.user_id = user_id