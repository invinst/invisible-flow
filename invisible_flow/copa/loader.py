import pandas as pd
from sqlalchemy.exc import IntegrityError

from invisible_flow.copa.data_officer_allegation import DataOfficerAllegation
from manage import db
from invisible_flow.copa.data_allegation import DataAllegation
from invisible_flow.copa.data_officer_unknown import DataOfficerUnknown  # noqa: F401


class Loader:

    def __init__(self):
        self.existing_crids = []
        self.existing_beat_ids = []
        self.crids = []
        self.beat_ids = []
        self.new_data = pd.DataFrame(columns=['crid','beat_id'])

    def load_into_db(self, transformed_data: pd.DataFrame):
        for row in transformed_data.itertuples():
            if 'beat_id' in transformed_data.columns.values:
                new_allegation = DataAllegation(crid=row.cr_id, cr_id=row.cr_id, beat_id=row.beat_id)
            else:
                new_allegation = DataAllegation(crid=row.cr_id, cr_id=row.cr_id)
            db.session.add(new_allegation)
            try:
                db.session.commit()
                self.load_officer_allegation_rows_into_db(row.number_of_officer_rows, row.cr_id)
                db.session.commit()
            except IntegrityError:
                self.existing_crids.append(pd.Series(transformed_data.iloc[row[0]][0]))
                self.beat_ids.append(pd.Series(transformed_data.iloc[row[0]][0]))

                db.session.rollback()
            else:
                #assumes crid and beat_ids match at all times
                self.crids.append(transformed_data.iloc[row[0]][0])
                self.beat_ids.append(transformed_data.iloc[row[0]][2])

        self.new_data = pd.DataFrame({'crid':self.crids,'beat_id':self.beat_ids})
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
        return pd.DataFrame({'crid':self.existing_crids,'beat_id':self.existing_beat_ids})

    def get_new_data(self):
        return self.new_data
