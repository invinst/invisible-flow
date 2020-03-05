import pandas as pd
from sqlalchemy.exc import IntegrityError

from manage import db
from invisible_flow.copa.data_allegation import DataAllegation


class Loader:

    def __init__(self):
        self.existing_crids = []
        self.new_data = []

    def load_into_db(self, transformed_data: pd.DataFrame):

        for row in transformed_data.itertuples():

            new_allegation = DataAllegation(cr_id=row.cr_id)
            db.session.add(new_allegation)
            try:
                db.session.commit()
            except IntegrityError:
                self.existing_crids.append(transformed_data.iloc[row[0]])
                db.session.rollback()
            else:
                self.new_data.append(transformed_data.iloc[row[0]])

        db.session.close()

    def get_matches(self):
        return self.existing_crids

    def get_new_data(self):
        return self.new_data
