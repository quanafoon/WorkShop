from App.database import db
from App.models import Internships, Applications, Shortlist

def getShortlists():
    shortlists = Shortlist.query.all()
    return shortlists

def findShortlist(id):
    shortlist = Shortlist.query.filter_by(id=id).first()
    return shortlist




