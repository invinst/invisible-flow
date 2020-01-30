from invisible_flow.constants import COPA_DB_BIND_KEY
from manage import db


class DataAllegationCategory(db.Model):
    __bind_key__ = COPA_DB_BIND_KEY
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255), nullable=False)
    category_code = db.Column(db.String(255), nullable=False)
    allegation_name = db.Column(db.String(255), nullable=False)
    on_duty = db.Column(db.Boolean, nullable=False)
    citizen_dept = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<DataAllegationCategory {self.id} ' \
               f'category: {self.category}, ' \
               f'category_code: {self.category_code}, ' \
               f'allegation_name: {self.allegation_name}, ' \
               f'on_duty: {self.on_duty}, ' \
               f'citizen_dept: {self.citizen_dept}, ' \
               f'created_at: {self.created_at}, ' \
               f'updated_at: {self.updated_at}, ' \
               f'>'


def insert_data_allegation_category_record_into_database(record: DataAllegationCategory):
    db.session.add(record)
    db.session.commit()
