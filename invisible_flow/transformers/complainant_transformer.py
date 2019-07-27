import datetime
import time

from typing import List

from invisible_flow.entities.data_allegation import Allegation
import pandas as pd
from io import StringIO

from invisible_flow.transformers.transformer_base import TransformerBase


class ComplainantTransformer(TransformerBase):

    def change_birth_year_to_age(self, row: pd.Series):
        # this function needs to be idempotent because df.apply is called twice for optimization reasons
        # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html
        row['age'] = datetime.datetime.now().year - row['BIRTH_YEAR']
        return row

    def transform(self, response_type: str, file_content: str) -> str:
        string_io_csv = StringIO(file_content)

        complainant_df = pd.read_csv(string_io_csv)
        complainant_df_with_renamed_columns = complainant_df \
            .drop(columns=['COMPLAINT_DATE', 'IAD_OPS', 'PARTY_TYPE', 'PARTY_SUBTYPE']) \
            .rename(columns={
                'LOG_NO': 'cr_id',
                'RACE': 'race',
                'SEX': 'gender'
            })

        final_complainant_df = complainant_df_with_renamed_columns \
            .apply(func=self.change_birth_year_to_age, axis=1) \
            .drop(columns='BIRTH_YEAR')

        # index=False removes leading column in dataframe that represents the df row number
        return final_complainant_df.to_csv(index=False)
