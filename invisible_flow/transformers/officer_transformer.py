import pdb
import numpy as np
import pandas as pd


class OfficerTransformer(object):

    def transform(self, new_rows: pd.DataFrame):
        self.transform_column_names(new_rows)
        officer_demographic_data = new_rows.filter(['allegation_id', 'age', 'gender', 'race', 'years_on_force'],
                                                   axis='columns')
        officer_allegation_data = new_rows.drop(['age', 'gender', 'race', 'years_on_force'], axis='columns')
        self.transform_gender_data(officer_demographic_data)
        return officer_demographic_data

    def transform_gender_data(self, officer_demographic_data: pd.DataFrame):
        officer_demographic_data.fillna('U')
        officer_demographic_data['gender'] = officer_demographic_data['gender'].apply(lambda x: x[:1] if x is not np.nan else 'U')
        # transformed_officer_columns.loc[transformed_officer_columns['gender'] == 'Male', 'gender'] = 'M'
        # transformed_officer_columns.loc[transformed_officer_columns['gender'] == 'Female', 'gender'] = 'F'
        # transformed_officer_columns.loc[(transformed_officer_columns['gender'] != 'M')
        #                                & (transformed_officer_columns['gender'] != 'F'), 'gender'] = 'U'

        return officer_demographic_data

    def transform_column_names(self, new_rows: pd.DataFrame):
        new_rows.rename(columns={
            "log_no": "allegation_id",
            "race_of_involved_officer": "race",
            "sex_of_involved_officer": "gender",
            "age_of_involved_officer": "age",
            "years_on_force_of_involved_officer": "years_on_force"
        }, inplace=True)

        return new_rows
