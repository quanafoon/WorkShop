from App.database import db

class Internships(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String, nullable=False)
    company = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120))
    start = db.Column(db.String(120))
    duration = db.Column(db.String(120))
    stipend = db.Column(db.String(120))
    company_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    applications = db.relationship('Applications', backref='internship', lazy=True, cascade='all, delete-orphan')
    shortlist = db.relationship('Shortlist', backref='internships', lazy=True, cascade='all, delete-orphan')


    def __init__(self, title, company, location, start, duration, stipend, company_id):
        self.title = title
        self.company = company
        self.location = location
        self.start = start
        self.duration = duration
        self.stipend = stipend
        self.company_id = company_id