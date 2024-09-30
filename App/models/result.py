from App.database import db

class Result(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    competition_id = db.Column(db.Integer,db.ForeignKey('competition.id'),nullable=False)
    participant_name = db.Column(db.String(255),nullable=False)
    score_percentage = db.Column(db.Integer,nullable=False)

    def __init__(self,participant_name,score_percentage):
        self.participant_name = participant_name
        self.score_percentage = score_percentage

    def __repr__(self):
        return (f'< Result: {self.id} Competition:  {self.competition.competition_name} Participant: {self.participant_name} Score: {self.score_percentage}>')