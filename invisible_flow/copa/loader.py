import pandas as pd

from invisible_flow.copa.data_officer_allegation import DataOfficerAllegation
from manage import db
from invisible_flow.copa.data_allegation import DataAllegation


class Loader:

    def __init__(self):
        self.existing_crid = pd.DataFrame(
            DataAllegation.query.with_entities(DataAllegation.cr_id)
        ).values.flatten().tolist()
        self.matches = []
        self.new_data = []

    def load_into_db(self, transformed_data: pd.DataFrame):

        for row in transformed_data.itertuples():

            if row.cr_id not in self.existing_crid:
                new_allegation = DataAllegation(cr_id=row.cr_id)
                db.session.add(new_allegation)
                self.load_officer_allegation_rows_into_db(row.number_of_officer_rows, row.cr_id)
                self.new_data.append(transformed_data.iloc[row[0]])
            else:
                self.matches.append(transformed_data.iloc[row[0]])

        db.session.commit()
        db.session.close()

    def load_officer_allegation_rows_into_db(self, number_of_rows: int, cr_id: str):
        for row_index in range(0, number_of_rows):
            new_officer_allegation = DataOfficerAllegation(
                allegation_id=cr_id,
                recc_finding="NA",
                recc_outcome="NA",
                final_finding="NA",
                final_outcome="NA",
                final_outcome_class="NA",
            )
            db.session.add(new_officer_allegation)



    def get_matches(self):
        return self.matches

    def get_new_data(self):
        return self.new_data
