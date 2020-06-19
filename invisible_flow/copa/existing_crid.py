from invisible_flow.constants import COPA_DB_BIND_KEY
from manage import db


class ExistingCrid(db.Model):
    __bind_key__ = COPA_DB_BIND_KEY
    __tablename__ = 'existing_crid'
    id = db.Column(db.Integer, nullable=True, primary_key=True)
    existing_crids = db.Column(db.String())

    def __repr__(self):
        return f'<id: {self.id}, ' \
               f'existing_crids: {self.existing_crids}, ' \
               f'>'


def insert_existing_crid_into_database(record: ExistingCrid):
    db.session.add(record)
    db.session.commit()
