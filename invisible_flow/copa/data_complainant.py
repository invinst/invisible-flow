from invisible_flow.constants import COPA_DB_BIND_KEY
from manage import db


class DataComplainant(db.Model):
    __bind_key__ = COPA_DB_BIND_KEY
    __tablename__ = 'data_complainant'
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(1), nullable=False)
    race = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)
    birth_year = db.Column(db.Integer)
    allegation_id = db.Column(db.String(30))
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<DataComplainant {self.id} ' \
               f'gender: {self.gender}, ' \
               f'race: {self.race}, ' \
               f'age: {self.age}, ' \
               f'birth_year: {self.birth_year}, ' \
               f'allegation_id: {self.allegation_id}, ' \
               f'created_at: {self.created_at}, ' \
               f'updated_at: {self.updated_at}, ' \
               f'>'


# def insert_officer_allegation_into_database(record: DataComplainant):
#     db.session.add(record)
#     db.session.commit()
