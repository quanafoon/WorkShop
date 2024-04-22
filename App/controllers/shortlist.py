from App.database import db
from App.models import Internships, Applications, Shortlist

def getShortlists():
    shortlists = Shortlist.query.all()
    return shortlists

def findShortlist(id):
    shortlist = Shortlist.query.filter_by(id=id).first()
    return shortlist

def addToShortlist(application_id, internship_id):
    check = Shortlist.query.filter_by(application_id=application_id).first()
    if check:
        return None
    else:
        shortlist = Shortlist(application_id=application_id, internship_id=internship_id)
        db.session.add(shortlist)
        db.session.commit()
        return shortlist
