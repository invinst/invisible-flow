import pdb

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
        self.match_data = pd.DataFrame(columns=['cr_id', 'beat_id'])
        self.new_data = pd.DataFrame(columns=['cr_id', 'beat_id'])

    def load_into_db(self, transformed_data: pd.DataFrame):
        for row in transformed_data.itertuples():
            if 'beat_id' in transformed_data.columns.values:
                new_allegation = DataAllegation(crid=row.cr_id, cr_id=row.cr_id, beat_id=row.beat_id)
            else:
                new_allegation = DataAllegation(crid=row.cr_id, cr_id=row.cr_id)
                db.session.add(new_allegation)
            try:
                db.session.commit()
                #pdb.set_trace()
                self.load_officer_allegation_rows_into_db(row.number_of_officer_rows, row.cr_id, row)
                self.load_officer_rows_into_db(row.officers)
                db.session.commit()
            except IntegrityError:
                self.existing_crids.append(transformed_data.iloc[row[0]][0])
                self.existing_beat_ids.append(transformed_data.iloc[row[0]][2])
                db.session.rollback()
            else:
                # assumes crid and beat_ids match at all times
                self.crids.append(transformed_data.iloc[row[0]][0])
                self.beat_ids.append(transformed_data.iloc[row[0]][2])

        self.new_data = pd.DataFrame({'cr_id': self.crids, 'beat_id': self.beat_ids})
        self.match_data = pd.DataFrame({'cr_id': self.existing_crids, 'beat_id': self.existing_beat_ids})
        db.session.close()


    def load_officer_rows_into_db(self, officer_rows: pd.Series):
        for (idx, officer) in officer_rows.items():
            new_officer = DataOfficerUnknown(
                age=officer['age'],
                race=officer['race'],
                gender=officer['gender'],
                years_on_force=officer['years_on_force']
            )
            db.session.add(new_officer)


    def load_officer_allegation_rows_into_db(self, number_of_rows: int, cr_id: str, row):
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
            db.session.commit()
            new_data_unknown_officer = DataOfficerUnknown(
                data_officerallegation_id=new_officer_allegation.id,
                age=row.officer_age[row_index],
                race=row.officer_race[row_index],
                gender=row.officer_gender[row_index]
            )
            db.session.add(new_data_unknown_officer)
            db.session.commit()


    def get_matches(self):
        return self.match_data

    def get_new_data(self):
        return self.new_data
