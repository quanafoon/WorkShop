from App.database import db
from App.models import Internships, Applications
import csv
'''
def parse_internships():
    with open('internships.csv', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)  
        header = next(csvreader)

        for row in csvreader: 
            internship_title = row[0]
            company_name = row[1]
            location = row[2]
            start_date = row[3]
            duration = row[4]
            stipend = row[5]

            internship = Internships(
                title=internship_title,
                company=company_name,
                location=location,
                start=start_date,
                duration=duration,
                stipend=stipend
            )
            db.session.add(internship)
        db.session.commit()
'''


def getInternships():
    internships = Internships.query.all()
    return internships

def findInternship(id):
    internship = Internships.query.filter_by(id=id).first()
    return internship

def apply(firstname, lastname, dob, email, phone, transcript_path, resume_path, user_id, internship_id):
    application = Applications(firstname=firstname, lastname=lastname, dob=dob, email=email, phone=phone, transcript=transcript_path, resume=resume_path, user_id=user_id, internship_id=internship_id)
    db.session.add(application)
    db.session.commit()
    return application

def getApplications():
    applications= Applications.query.all()
    return applications

def findApplication(id):
    application = Applications.query.filter_by(id=id).first()
    return application

def getAppsForInternship(id):
    applications= Applications.query.filter_by(internship_id=id).all()
    return applications

def addProject(title, company, company_id, location=None, start=None, duration=None, stipend=None):
    project = Internships(title=title, company=company, location=location, start=start, duration=duration, stipend=stipend, company_id=company_id)
    db.session.add(project)
    db.session.commit()
    return project

def deleteProject(id):
    internship = Internships.query.filter_by(id=id).first()
    if internship:
        db.session.delete(internship)
        db.session.commit()
    else:
        return None
    return internship