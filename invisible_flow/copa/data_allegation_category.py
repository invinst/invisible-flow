from invisible_flow.constants import COPA_DB_BIND_KEY
from manage import db


class AllegationCategory(db.Model):
    __bind_key__ = COPA_DB_BIND_KEY
    category = db.Column(db.String)
    category_code = db.Column(db.String)
    allegation_name = db.Column(db.String)
    on_duty = db.Column(db.String)
    cr_id = db.Column(db.String, primary_key=True)

    def __repr__(self):
        return f'<AllegationCategory {self.cr_id} ' \
               f'category: {self.category}, ' \
               f'category_code: {self.category_code}, ' \
               f'allegation_name: {self.allegation_name}, ' \
               f'on_duty: {self.on_duty}, ' \
               f'>'


def insert_allegation_category_record_into_database(record: AllegationCategory):
    db.session.add(record)
    db.session.commit()
