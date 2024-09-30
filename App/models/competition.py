from App.database import db
from datetime import datetime
from sqlalchemy.sql.expression import func

class Competition(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    competition_name = db.Column(db.String(255),unique=True,nullable=False)
    date = db.Column(db.DateTime,default=func.now())
    results = db.relationship('Result',backref='competition',lazy=True,cascade='all, delete-orphan')

    def __init__(self,competition_name,date = None):
        self.competition_name = competition_name
        self.date = date or datetime.now()

    def __repr__(self):
        return (f'< Competition: {self.id} - {self.competition_name} - {self.date}')
        

