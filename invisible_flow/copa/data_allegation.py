from invisible_flow.constants import COPA_DB_BIND_KEY
from manage import db
from geoalchemy2 import Geometry

from sqlalchemy.dialects import postgresql


class DataAllegation(db.Model):
    __bind_key__ = COPA_DB_BIND_KEY
    id = db.Column(db.Integer, primary_key=True)
    cr_id = db.Column(db.String(30), nullable=False)
    summary = db.Column(db.Text, nullable=False)
    add1 = db.Column(db.String(16), nullable=False)
    add2 = db.Column(db.String(255), nullable=False)
    beat_id = db.Column(db.Integer)
    city = db.Column(db.String(255), nullable=False)
    incident_date = db.Column(db.DateTime)
    is_officer_complaint = db.Column(db.Boolean, nullable=False)
    location = db.Column(db.String(64), nullable=False)
    old_complaint_address = db.Column(db.String(255))
    subjects = db.Column(postgresql.ARRAY(db.String), nullable=False)
    point = db.Column(Geometry(geometry_type='POINT', srid=4326))
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<DataAllegation {self.id} ' \
               f'cr_id: {self.cr_id}, ' \
               f'summary: {self.summary}, ' \
               f'add1: {self.add1}, ' \
               f'add2: {self.add2}, ' \
               f'beat_id: {self.beat_id}, ' \
               f'city: {self.city}, ' \
               f'incident_date {self.incident_date}, ' \
               f'is_officer_complaint: {self.is_officer_complaint}, ' \
               f'location: {self.location}, ' \
               f'old_complaint_address: {self.old_complaint_address}, ' \
               f'subjects: {self.subjects}, ' \
               f'point: {self.point}, ' \
               f'created_at: {self.created_at}, ' \
               f'updated_at: {self.updated_at}, ' \
               f'>'

    # enables subscriptability like Allegation['beat_id'] instead of forcing
    # Allegation.beat_id syntax
    def __getitem__(self, index):
        return self.__getattribute__(index)


def insert_allegation_into_database(record: DataAllegation):
    db.session.add(record)
    db.session.commit()
