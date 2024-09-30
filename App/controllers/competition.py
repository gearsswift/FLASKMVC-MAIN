from sqlalchemy.exc import IntegrityError
from App.models.result import Result
from App.models.competition import Competition
from App.database import db
from datetime import datetime
import csv

def create_competition(competition_name,date=None):
    date = date or datetime.now()
    competition = Competition(competition_name,date)
      # Try to add the user to the database
    try:
        db.session.add(competition)
        db.session.commit()
    except IntegrityError as e:
        # Rollback if there is a unique constraint violation (e.g., duplicate username or email)
        db.session.rollback()
        return None
    else:
        # Print the newly created user details
        return competition

def get_competitions():
   return Competition.query.all()

def add_competition_result(competition_id,participant,participant_score):
    entered_result = Result(participant,participant_score)
    competition = Competition.query.filter_by(id = competition_id).first()
    if not competition:
        return
    
    competition.results.append(entered_result)
    db.session.add(competition)
    db.session.commit()
    return competition


def add_competition_results_from_csv(competition_id,filepath):
    competition = Competition.query.filter_by(id = competition_id).first()
    if not competition:
        print(f'Competition at {competition_id} does not exist')
        return

    try:
        with open(filepath,'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            for line in csv_reader:
                entered_result = Result(line[0],int(line[1]))
                competition.results.append(entered_result)
    except:
        return ["Error reading from file"]
    
   
    db.session.add(competition)
    db.session.commit()
    return competition

def get_competition_results(competition_id):
    competition = Competition.query.filter_by(id = competition_id).first()
    if not competition:
        print(f'Competition at {competition_id} does not exist')
        return
    if competition.results != None:
        return competition.results
    else:
        return []