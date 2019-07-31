from typing import List, Tuple

import pandas as pd
from io import StringIO

from invisible_flow.transformers.transformer_base import TransformerBase


class AccusedTransformer(TransformerBase):

    def transform(self, response_type: str, csv_content: str) -> List[Tuple[str, str]]:
        string_io_csv = StringIO(csv_content)
        accused_df = pd.read_csv(string_io_csv)
        allegationcategory_columns = [
            'ALLEGATION_CATEGORY',
            'ALLEGATION_CATEGORY_CD',
            'LOG_NO'
        ]
        officer_columns = [
            'BIRTH_YEAR',
            'OFFICER_FIRST_NAME',
            'SEX_CODE_CD',
            'OFFICER_LAST_NAME',
            'MIDDLE_INITIAL',
            'RACE_CODE_CD',
            'EMPLOYEE_POSITION',
            'LOG_NO'
        ]
        officerbadgenumber_columns = [
            'EMPLOYEE_NO',
            'STAR_NO',
            'LOG_NO'
        ]
        policeunit_columns = [
            'EMPLOYEE_DETAIL_UNIT',
            'EMPLOYEE_ASSIGN_UNIT',
            'LOG_NO'
        ]
        return [
            (
                'allegationcategory',
                accused_df.loc[:, allegationcategory_columns].rename(columns={
                    allegationcategory_columns[0]: 'category',
                    allegationcategory_columns[1]: 'category_code',
                    allegationcategory_columns[2]: 'cr_id'
                }).to_csv(index=False)
            ), (
                'officer',
                accused_df.loc[:, officer_columns].rename(columns={
                    officer_columns[0]: 'birth_year',
                    officer_columns[1]: 'first_name',
                    officer_columns[2]: 'gender',
                    officer_columns[3]: 'last_name',
                    officer_columns[4]: 'middle_initial',
                    officer_columns[5]: 'race',
                    officer_columns[6]: 'rank',
                    officer_columns[7]: 'cr_id'
                }).to_csv(index=False)
            ), (
                'officerbadgenumber',
                accused_df.loc[:, officerbadgenumber_columns].rename(columns={
                    officerbadgenumber_columns[0]: 'officer_id',
                    officerbadgenumber_columns[1]: 'star',
                    officerbadgenumber_columns[2]: 'cr_id'
                }).to_csv(index=False)
            ), (
                'policeunit',
                accused_df.loc[:, policeunit_columns].rename(columns={
                    policeunit_columns[0]: 'tags',
                    policeunit_columns[1]: 'unit_name',
                    policeunit_columns[2]: 'cr_id'
                }).to_csv(index=False)
            )
        ]
