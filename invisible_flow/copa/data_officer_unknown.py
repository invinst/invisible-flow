from invisible_flow.constants import COPA_DB_BIND_KEY
from manage import db
from datetime import datetime


class DataOfficerUnknown(db.Model):
    __bind_key__ = COPA_DB_BIND_KEY
    __tablename__ = 'data_officerunknown'
    id = db.Column(db.Integer, nullable=True, primary_key=True)
    data_officerallegation_id = db.Column(db.Integer)
    age = db.Column(db.String(50))
    gender = db.Column(db.String(1), nullable=True)
    race = db.Column(db.String(50), nullable=True)
    years_on_force = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<id: {self.id}, ' \
               f'data_officerallegation_id: {self.data_officerallegation_id}, ' \
               f'age: {self.age}, ' \
               f'gender: {self.gender}, ' \
               f'race: {self.race}, ' \
               f'years_on_force: {self.years_on_force}, ' \
               f'created_at: {self.created_at}, ' \
               f'updated_at: {self.updated_at}, ' \
               f'>'


def insert_officerunknown_into_database(record: DataOfficerUnknown):
    db.session.add(record)
    db.session.commit()
