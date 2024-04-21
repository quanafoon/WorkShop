from App.database import db

class Internships(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String, nullable=False)
    company = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120))
    start = db.Column(db.String(120))
    duration = db.Column(db.String(120))
    stipend = db.Column(db.String(120))



    def __init__(self, title, company, location, start, duration, stipend):
        self.title = title
        self.company = company
        self.location = location
        self.start = start
        self.duration = duration
        self.stipend = stipend