from invisible_flow.constants import COPA_DB_BIND_KEY
from manage import db


class CopaRecord(db.Model):
    __bind_key__ = COPA_DB_BIND_KEY
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)

    def __repr__(self):
        return f'<CopaRecord {self.id} status: {self.status}>'


def insert_copa_record_into_database(record: CopaRecord):
    db.session.add(record)
    db.session.commit()
