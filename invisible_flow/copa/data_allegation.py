from invisible_flow.constants import COPA_DB_BIND_KEY
from manage import db
from datetime import datetime
# These libraries lack mypy typing
from geoalchemy2 import Geometry  # type: ignore
from sqlalchemy.dialects import postgresql  # type: ignore


class DataAllegation(db.Model):
    __bind_key__ = COPA_DB_BIND_KEY
    cr_id = db.Column(db.String(30), nullable=False, primary_key=True)
    crid = db.Column(db.String(30))
    summary = db.Column(db.Text, nullable=False, default='')
    add1 = db.Column(db.String(16), nullable=False, default='')
    add2 = db.Column(db.String(255), nullable=False, default='')
    source = db.Column(db.String(255), nullable=False, default='')
    beat_id = db.Column(db.String())
    city = db.Column(db.String(255), nullable=False, default='')
    incident_date = db.Column(db.DateTime)
    is_officer_complaint = db.Column(db.Boolean, nullable=False, default=False)
    location = db.Column(db.String(64), nullable=False, default='')
    old_complaint_address = db.Column(db.String(255))
    subjects = db.Column(postgresql.ARRAY(db.String), nullable=False, default=[])
    point = db.Column(Geometry(geometry_type='POINT', srid=4326))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<cr_id: {self.cr_id}, ' \
               f'crid: {self.crid}, ' \
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
