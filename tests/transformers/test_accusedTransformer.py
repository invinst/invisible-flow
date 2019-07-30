import pandas as pd
from invisible_flow.transformers.accused_transformer import AccusedTransformer

from invisible_flow.entities.data_allegationcategory import AllegationCategory
from invisible_flow.entities.data_officer import Officer
from invisible_flow.entities.data_officerbadgenumber import OfficerBadgeNumber
from invisible_flow.entities.data_policeunit import PoliceUnit


class TestAccusedTransformer:

    def test_csv_to_entity_name_entity_list_tuples(self):
        transformer = AccusedTransformer()
        df = pd.DataFrame(
            [
                [
                    'moo1',
                    'cow1',
                    True,
                    '24',
                    1994,
                    'Jeff',
                    'M',
                    'Burroughs',
                    'N',
                    'WHI',
                    'SERGEANT OF POLICE',
                    '122',
                    '654',
                    '3',
                    'detail unit'
                ],
                [
                    'moo2',
                    'cow2',
                    True,
                    '25',
                    1994,
                    'Joe',
                    'M',
                    'Mo',
                    'N',
                    'WHI',
                    'POLICE OFFICER',
                    '122',
                    '654',
                    '3',
                    'detail unit'
                ]
            ],
            columns=[
                'ALLEGATION_CATEGORY',
                'ALLEGATION_CATEGORY_CD',
                'EMPLOYEE_ON_DUTY',
                'LOG_NO',
                'BIRTH_YEAR',
                'OFFICER_FIRST_NAME',
                'SEX_CODE_CD',
                'OFFICER_LAST_NAME',
                'MIDDLE_INITIAL',
                'RACE_CODE_CD',
                'EMPLOYEE_POSITION',
                'EMPLOYEE_NO',
                'STAR_NO',
                'EMPLOYEE_DETAIL_UNIT',
                'EMPLOYEE_ASSIGN_UNIT'
            ]
        )

        actual_result = transformer.csv_to_entity_name_entity_list_tuples(df)
        expected_result = [
            (
                'allegationcategory',
                AllegationCategory(
                    category='0    moo1\n1    moo2\nName: ALLEGATION_CATEGORY, dtype: object',
                    category_code='0    cow1\n1    cow2\nName: ALLEGATION_CATEGORY_CD, dtype: object',
                    on_duty=False,
                    cr_id='0    24\n1    25\nName: LOG_NO, dtype: object'
                )
            ),
            (
                'officer',
                Officer(
                    birth_year='0    1994\n1    1994\nName: BIRTH_YEAR, dtype: int64',
                    first_name='0    Jeff\n1     Joe\nName: OFFICER_FIRST_NAME, dtype: object',
                    gender='0    M\n1    M\nName: SEX_CODE_CD, dtype: object',
                    last_name='0    Burroughs\n1           Mo\nName: OFFICER_LAST_NAME, dtype: object',
                    middle_initial='0    N\n1    N\nName: MIDDLE_INITIAL, dtype: object',
                    race='0    WHI\n1    WHI\nName: RACE_CODE_CD, dtype: object',
                    rank='0    SERGEANT OF POLICE\n1        POLICE OFFICER\nName: EMPLOYEE_POSITION, dtype: object',
                    cr_id='0    24\n1    25\nName: LOG_NO, dtype: object')
            ),
            (
                'officerbadgenumber',
                OfficerBadgeNumber(
                    officer_id='0    122\n1    122\nName: EMPLOYEE_NO, dtype: object',
                    star='0    654\n1    654\nName: STAR_NO, dtype: object',
                    cr_id='0    24\n1    25\nName: LOG_NO, dtype: object')
            ),
            (
                'policeunit',
                PoliceUnit(
                    tags='0    3\n1    3\nName: EMPLOYEE_DETAIL_UNIT, dtype: object',
                    unit_name='0    detail unit\n1    detail unit\nName: EMPLOYEE_ASSIGN_UNIT, dtype: object',
                    cr_id='0    24\n1    25\nName: LOG_NO, dtype: object')
            )
        ]

        assert actual_result == expected_result
