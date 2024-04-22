from App.database import db
from .applications import Applications
from .internships import Internships

class Shortlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    internship_id = db.Column(db.Integer, db.ForeignKey('internships.id'), nullable=False)
    application_id = db.Column(db.Integer, db.ForeignKey('applications.id'), nullable=False)
    internship = db.relationship('Internships', backref='shortlists', lazy=True)
    application = db.relationship('Applications', backref='shortlists', lazy=True)

    def __init__(self, internship_id, application_id):
        self.internship_id = internship_id
        self.application_id = application_id
