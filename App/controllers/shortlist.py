from App.database import db
from App.models import Internships, Applications, Shortlist
import csv

def parse_shortlists():
    with open('shortlists.csv', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)  
        header = next(csvreader)

        for row in csvreader: 
            internship_id = row[0]
            application_id = row[1]

            shortlist = Shortlist(
                internship_id=internship_id,
                application_id=application_id
            )
            db.session.add(shortlist)
        db.session.commit()

def getShortlists():
    shortlists = Shortlist.query.all()
    return shortlists

def findShortlist(id):
    shortlist = Shortlist.query.filter_by(id=id).first()
    return shortlist

def getShortlistForInternship(id):
    shortlist = Shortlist.query.filter_by(internship_id=id).all()
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
