import pdb
import numpy as np
import pandas as pd
from invisible_flow.constants import RACE_MAPPER


class OfficerTransformer(object):

    def transform(self, new_rows: pd.DataFrame):
        self.transform_column_names(new_rows)
        self.add_derived_columns(new_rows)
        officer_demographic_data = new_rows.filter(['allegation_id', 'age', 'gender', 'race', 'years_on_force'],
                                                   axis='columns')
        self.transform_gender_data(officer_demographic_data)
        self.transform_race_data(officer_demographic_data)
        officer_allegation_data = new_rows.drop(['age', 'gender', 'race', 'years_on_force'], axis='columns')
        return officer_demographic_data, officer_allegation_data

    def transform_gender_data(self, officer_demographic_data: pd.DataFrame):
        officer_demographic_data['gender'] = officer_demographic_data['gender'].apply(lambda x: x[:1] if x is not np.nan else 'U')
        return officer_demographic_data

    def transform_race_data(self, officer_demographic_data: pd.DataFrame):
        def map_race(race):
            try:
                return RACE_MAPPER[race]
            except KeyError:
                return "Unknown"

        officer_demographic_data['race'] = officer_demographic_data['race'].apply(lambda x: map_race(x))
        return officer_demographic_data

    def transform_column_names(self, new_rows: pd.DataFrame):
        new_rows.rename(columns={
            "log_no": "allegation_id",
            "complaint_date": "start_date",
            "finding_code": "recc_finding",
            "race_of_involved_officer": "race",
            "sex_of_involved_officer": "gender",
            "age_of_involved_officer": "age",
            "years_on_force_of_involved_officer": "years_on_force"
        }, inplace=True)
        return new_rows

    def add_derived_columns(self, new_rows: pd. DataFrame):
        new_rows['final_finding'] = new_rows['recc_finding']
        return new_rows
