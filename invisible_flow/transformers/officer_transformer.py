import pdb

import pandas as pd


class OfficerTransformer(object):

    def transform_officer_column_names(self, new_rows: pd.DataFrame):

        new_rows.rename(columns={
            "log_no": "allegation_id",
            "race_of_involved_officer": "race",
            "sex_of_involved_officer": "gender",
            "age_of_involved_officer": "age",
            "years_on_force_of_involved_officer": "years_on_force"
        }, inplace=True)

        # self.transform_gender_data(new_rows)
        return new_rows

    def transform_gender_data(self, transformed_officer_columns: pd.DataFrame):
        transformed_officer_columns.loc[transformed_officer_columns['gender'] == 'Male', 'gender'] = 'M'
        transformed_officer_columns.loc[transformed_officer_columns['gender'] == 'Female', 'gender'] = 'F'
        transformed_officer_columns.fillna('U', inplace=True)

        return transformed_officer_columns