from invisible_flow.constants import COPA_DB_BIND_KEY
from manage import db


class DataOfficerAllegation(db.Model):
    __bind_key__ = COPA_DB_BIND_KEY
    __tablename__ = 'data_officer_allegation'
    id = db.Column(db.Integer, primary_key=True)
    allegation_id = db.Column(db.String(30))
    allegation_category_id = db.Column(db.Integer)
    officer_id = db.Column(db.Integer)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    officer_age = db.Column(db.Integer)
    recc_finding = db.Column(db.String(2), nullable=False)
    recc_outcome = db.Column(db.String(32), nullable=False)
    final_finding = db.Column(db.String(2), nullable=False)
    final_outcome = db.Column(db.String(32), nullable=False)
    final_outcome_class = db.Column(db.String(20), nullable=False)
    disciplined = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<OfficerAllegation {self.id} ' \
               f'allegation_id: {self.allegation_id}, ' \
               f'allegation_category_id: {self.allegation_category_id}, ' \
               f'officer_id: {self.officer_id}, ' \
               f'start_date: {self.start_date}, ' \
               f'end_date: {self.end_date}, ' \
               f'officer_age: {self.officer_age}, ' \
               f'recc_finding: {self.recc_finding}, ' \
               f'final_finding: {self.final_finding}, ' \
               f'final_outcome: {self.final_outcome}, ' \
               f'final_outcome_class: {self.final_outcome_class}, ' \
               f'disciplined: {self.disciplined}, ' \
               f'created_at: {self.created_at}, ' \
               f'updated_at: {self.updated_at}, ' \
               f'>'


def insert_complainant_into_database(record: DataOfficerAllegation):
    db.session.add(record)
    db.session.commit()
