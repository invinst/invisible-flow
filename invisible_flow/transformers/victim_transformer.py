from io import StringIO
from typing import List, Tuple

import pandas as pd

from invisible_flow.transformers.transformer_base import TransformerBase


class VictimTransformer(TransformerBase):
    def change_birth_year_to_age_at_incident(self, row: pd.Series):
        # this function needs to be idempotent because df.apply is called twice for optimization reasons
        # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html
        row['age_at_incident'] = ''
        return row

    def change_sex_to_one_letter(self, row: pd.Series):
        sex_dict = {'MALE': 'M', 'FEMALE': 'F'}
        row['gender'] = sex_dict.get(row['SEX'], '')
        return row

    def transform(self, response_type: str, file_content: str) -> List[Tuple[str, str]]:
        string_io_csv = StringIO(file_content)

        victim_df = pd.read_csv(string_io_csv)
        victim_df_with_age = victim_df.apply(func=self.change_birth_year_to_age_at_incident, axis='columns')\
            .apply(func=self.change_sex_to_one_letter, axis='columns')
        final_victim_df = victim_df_with_age \
            .drop(columns=['COMPLAINT_DATE', 'IAD_OPS', 'PARTY_TYPE', 'PARTY_SUBTYPE', 'PARTY_INJURED',
                           'INJURY_CONDITION', 'INJURY_DESCRIPTION', 'SEX']) \
            .rename(columns={
                'LOG_NO': 'crid',
                'RACE': 'race',
                'BIRTH_YEAR': 'birth_year'
            })

        return [(response_type, final_victim_df.to_csv(index=False))]
