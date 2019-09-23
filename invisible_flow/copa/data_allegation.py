from invisible_flow.constants import COPA_DB_BIND_KEY
from manage import db


class Allegation(db.Model):
    __bind_key__ = COPA_DB_BIND_KEY
    add1 = db.Column(db.String)
    add2 = db.Column(db.String)
    beat_id = db.Column(db.String)
    city = db.Column(db.String)
    incident_date = db.Column(db.String)
    is_officer_complaint = db.Column(db.Boolean)
    location = db.Column(db.String)
    summary = db.Column(db.String)
    cr_id = db.Column(db.String, primary_key=True)

    def __repr__(self):
        return f'<Allegation {self.cr_id} ' \
               f'add1: {self.add1}, ' \
               f'add2: {self.add2}, ' \
               f'beat_id: {self.beat_id}, ' \
               f'city: {self.city}, ' \
               f'incident_date: {self.incident_date}, ' \
               f'is_officer_complaint: {self.is_officer_complaint}, ' \
               f'location: {self.location}, ' \
               f'summary: {self.summary}, ' \
               f'>'

    # enables subscriptability like Allegation['beat_id'] instead of forcing
    # Allegation.beat_id syntax
    def __getitem__(self, index):
        return self.__getattribute__(index)


def insert_allegation_into_database(record: Allegation):
    db.session.add(record)
    db.session.commit()
