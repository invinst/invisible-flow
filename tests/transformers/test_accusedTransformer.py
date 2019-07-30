import pandas as pd
from invisible_flow.transformers.accused_transformer import AccusedTransformer


class TestAccusedTransformer:

    def test_csv_to_entity_name_entity_list_tuples(self):
        transformer = AccusedTransformer()
        expected_df = pd.DataFrame(
            [
                ['moo1', 'cow1', True, '24', 1994, 'Jeff', 'M', 'Burroughs', 'N', 'WHI', 'SERGEANT OF POLICE', '122', '654', '3', 'detail unit'],
                ['moo2', 'cow2', True, '25', 1994, 'Joe', 'M', 'Mo', 'N', 'WHI', 'POLICE OFFICER', '122', '654', '3', 'detail unit']
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
        print('')
        print(expected_df)

        print(transformer.csv_to_entity_name_entity_list_tuples(expected_df))