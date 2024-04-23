from App.database import db
from .user import User
from .internships import Internships

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
    internship_id = db.Column(db.Integer, db.ForeignKey('internships.id'), nullable=False)
    shortlist = db.relationship('Shortlist', backref='application', lazy=True, cascade='all, delete-orphan')


    def __init__(self, firstname, lastname, dob, email, phone, transcript, resume, user_id, internship_id):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.email = email
        self.phone = phone
        self.transcript = transcript
        self.resume = resume
        self.user_id = user_id
        self.internship_id = internship_id