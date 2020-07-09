import pandas as pd


class OfficerTransformer(object):
    def transform(self, new_rows: pd.DataFrame):
        new_rows.rename(columns={
            "log_no": "allegation_id",
            "race_of_involved_officer": "race",
            "sex_of_involved_officer": "gender",
            "age_of_involved_officer": "age",
            "years_on_force_of_involved_officer": "years_on_force"
        }, inplace=True)
        return new_rows
