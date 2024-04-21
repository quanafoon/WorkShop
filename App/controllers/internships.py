from App.database import db
from App.models import Internships
import csv

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

