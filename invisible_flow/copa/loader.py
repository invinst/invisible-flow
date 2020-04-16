import pandas as pd
from sqlalchemy.exc import IntegrityError

from invisible_flow.copa.data_officer_allegation import DataOfficerAllegation
from manage import db
from invisible_flow.copa.data_allegation import DataAllegation


class Loader:

    def __init__(self):
        self.existing_crids = []
        self.new_data = []

    def load_into_db(self, transformed_data: pd.DataFrame):
        for row in transformed_data.itertuples():
            if 'beat_id' in transformed_data.columns.values:
                new_allegation = DataAllegation(crid=row.crid, beat_id=row.beat_id)
            else:
                new_allegation = DataAllegation(crid=row.crid)
            db.session.add(new_allegation)
            try:
                db.session.commit()
                self.load_officer_allegation_rows_into_db(row.number_of_officer_rows, row.crid)
                db.session.commit()
            except IntegrityError:
                self.existing_crids.append(pd.Series(transformed_data.iloc[row[0]][0]))
                db.session.rollback()
            else:
                self.new_data.append(pd.Series(transformed_data.iloc[row[0]][0]))
        db.session.close()

    def load_officer_allegation_rows_into_db(self, number_of_rows: int, crid: str):
        for row_index in range(0, number_of_rows):
            new_officer_allegation = DataOfficerAllegation(
                allegation_id=crid,
                recc_finding="NA",
                recc_outcome="NA",
                final_finding="NA",
                final_outcome="NA",
                final_outcome_class="NA",
            )
            db.session.add(new_officer_allegation)

    def get_matches(self):
        return self.existing_crids

    def get_new_data(self):
        return self.new_data
