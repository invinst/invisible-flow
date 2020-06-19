import pandas as pd
from sqlalchemy.exc import IntegrityError

from invisible_flow.copa.converter import convert_sql_alchemy_obj_to_dict
from invisible_flow.copa.data_officer_allegation import DataOfficerAllegation
from manage import db
from invisible_flow.copa.data_allegation import DataAllegation
from invisible_flow.copa.data_officer_unknown import DataOfficerUnknown  # noqa: F401


class Loader:

    def __init__(self):
        self.match_allegation_data = pd.DataFrame(columns=['cr_id', 'beat_id'])
        self.new_allegation_data = pd.DataFrame(columns=['cr_id', 'beat_id'])
        self.new_officer_allegation_data = pd.DataFrame()
        self.new_officer_unknown_data = pd.DataFrame(columns=['data_officerallegation_id'])
        self.new_officer_unknown_data.data_officerallegation_id.astype('int64')

    def load_into_db(self, transformed_data: pd.DataFrame):
        for row in transformed_data.itertuples():
            new_allegation = DataAllegation(crid=row.cr_id, cr_id=row.cr_id, beat_id=row.beat_id)
            allegation_as_dict = convert_sql_alchemy_obj_to_dict(new_allegation)
            allegation_as_dict.pop("crid")  # removing the duplicate crid for csv
            db.session.add(new_allegation)

            try:  # Save cr_id to db
                db.session.commit()
                # ^This will throw an IntegrityError if the datallegation already exists in the database
            except IntegrityError:  # if cr_id in db, put in "existing" dataframe (i.e. match data csv)
                self.match_allegation_data = self.match_allegation_data.append(
                    allegation_as_dict, ignore_index=True)
                db.session.rollback()
            else:  # else put in "new" dataframe (i.e. new data csv)
                self.new_allegation_data = self.new_allegation_data.append(
                    allegation_as_dict, ignore_index=True)
                self.load_officers_into_db(row.number_of_officer_rows, row.cr_id, row)
        db.session.close()

    def load_officers_into_db(self, number_of_rows: int, cr_id: str, row: pd.DataFrame):
        for row_index in range(0, number_of_rows):
            new_officer_allegation = DataOfficerAllegation(
                allegation_id=cr_id,
                recc_finding="NA",
                recc_outcome="NA",
                final_finding="NA",
                final_outcome="NA",
                final_outcome_class="NA",
            )

            officer_allegation_as_dict = convert_sql_alchemy_obj_to_dict(new_officer_allegation)
            self.new_officer_allegation_data = self.new_officer_allegation_data.append(officer_allegation_as_dict,
                                                                                       ignore_index=True)

            db.session.add(new_officer_allegation)
            db.session.commit()

            if len(row.officer_age) >= 1:
                new_data_unknown_officer = DataOfficerUnknown(
                    data_officerallegation_id=new_officer_allegation.id,
                    age=row.officer_age[row_index],
                    race=row.officer_race[row_index],
                    gender=row.officer_gender[row_index],
                    years_on_force=row.officer_years_on_force[row_index]
                )

                unknown_officer_as_dict = convert_sql_alchemy_obj_to_dict(new_data_unknown_officer)
                self.new_officer_unknown_data = self.new_officer_unknown_data.append(unknown_officer_as_dict,
                                                                                     ignore_index=True)

                db.session.add(new_data_unknown_officer)
                db.session.commit()

    def get_allegation_matches(self):
        return self.match_allegation_data

    def get_new_allegation_data(self):
        return self.new_allegation_data
