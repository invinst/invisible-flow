import os

from invisible_flow.transformers.accused_transformer import AccusedTransformer

from invisible_flow.entities.data_allegationcategory import AllegationCategory
from invisible_flow.entities.data_officer import Officer
from invisible_flow.entities.data_officerbadgenumber import OfficerBadgeNumber
from invisible_flow.entities.data_policeunit import PoliceUnit


from tests.helpers.if_test_base import IFTestBase


class TestAccusedTransformer:

    def test_csv_to_entity_name_entity_list_tuples_head(self):
        transformer = AccusedTransformer()
        head_accused_path = os.path.join(IFTestBase.resource_directory, 'accused_head.csv')

        with open(head_accused_path) as file:
            actual_result = transformer.csv_to_entity_name_entity_list_tuples(file.read())

            # print('***********')
            print(actual_result[0][1])
            # print('***********')

    def test_csv_to_entity_name_entity_list_tuples_single(self):
        transformer = AccusedTransformer()
        head_accused_path = os.path.join(IFTestBase.resource_directory, 'accused_single_row.csv')

        with open(head_accused_path) as file:

            actual_result = transformer.csv_to_entity_name_entity_list_tuples(file.read())
            expected_result = [
                (
                    'allegationcategory',
                    AllegationCategory(
                        category='0    EXCESSIVE FORCE / ON DUTY - INJURY\nName: ALLEGATION_CATEGORY, dtype: object',
                        category_code='0    05A\nName: ALLEGATION_CATEGORY_CD, dtype: object',
                        on_duty=False,
                        cr_id='0    259794\nName: LOG_NO, dtype: int64')
                ), (
                    'officer',
                    Officer(
                        birth_year='0    1946\nName: BIRTH_YEAR, dtype: int64',
                        first_name='0    EARL\nName: OFFICER_FIRST_NAME, dtype: object',
                        gender='0    M\nName: SEX_CODE_CD, dtype: object',
                        last_name='0    WASHINGTON\nName: OFFICER_LAST_NAME, dtype: object',
                        middle_initial='0    B\nName: MIDDLE_INITIAL, dtype: object',
                        race='0    BLK\nName: RACE_CODE_CD, dtype: object',
                        rank='0    SERGEANT OF POLICE\nName: EMPLOYEE_POSITION, dtype: object',
                        cr_id='0    259794\nName: LOG_NO, dtype: int64')
                ), (
                    'officerbadgenumber',
                    OfficerBadgeNumber(
                        officer_id='0    1088\nName: EMPLOYEE_NO, dtype: int64',
                        star='0    1986\nName: STAR_NO, dtype: int64',
                        cr_id='0    259794\nName: LOG_NO, dtype: int64')
                ), (
                    'policeunit',
                    PoliceUnit(
                        tags='0    3\nName: EMPLOYEE_DETAIL_UNIT, dtype: int64',
                        unit_name='0   NaN\nName: EMPLOYEE_ASSIGN_UNIT, dtype: float64',
                        cr_id='0    259794\nName: LOG_NO, dtype: int64')
                )
            ]
            assert actual_result == expected_result

    def test_csv_to_entity_name_csv_tuples_head(self):
        transformer = AccusedTransformer()
        head_accused_path = os.path.join(IFTestBase.resource_directory, 'accused_head.csv')

        with open(head_accused_path) as file:
            expected_result = [
                ('allegationcategory', 'category,category_code,cr_id\nEXCESSIVE FORCE / ON DUTY - INJURY,05A,259794\nEXCESSIVE FORCE / ON DUTY - INJURY,05A,259794\nUNNECESSARY PHYSICAL CONTACT -ON DUTY,05ZZL,259797\nEXCESSIVE FORCE - USE OF FIREARM / OFF DUTY - INJURY,05G,259804\nEXCESSIVE FORCE - USE OF FIREARM / OFF DUTY - INJURY,05G,259804\nEXCESSIVE FORCE - USE OF FIREARM / OFF DUTY - INJURY,05G,259804\nEXCESSIVE FORCE - USE OF FIREARM / OFF DUTY - INJURY,05G,259804\nEXCESSIVE FORCE - USE OF FIREARM / OFF DUTY - INJURY,05G,259804\nEXCESSIVE FORCE - USE OF FIREARM / OFF DUTY - INJURY,05G,259804\n'),  # noqa: E501
                ('officer', 'birth_year,first_name,gender,last_name,middle_initial,race,rank,cr_id\n1946.0,EARL,M,WASHINGTON,B,BLK,SERGEANT OF POLICE,259794\n1963.0,TOMMY,M,BOUIE,D,BLK,POLICE OFFICER,259794\n,,,,,,,259797\n1955.0,KENNETH,M,MALKOWSKI,J,WHI,POLICE OFFICER,259804\n1955.0,KENNETH,M,MALKOWSKI,J,WHI,POLICE OFFICER,259804\n1955.0,KENNETH,M,MALKOWSKI,J,WHI,POLICE OFFICER,259804\n1955.0,KENNETH,M,MALKOWSKI,J,WHI,POLICE OFFICER,259804\n1963.0,ARTHUR,M,DAVIS JR,,BLK,POLICE OFFICER,259804\n1955.0,KENNETH,M,MALKOWSKI,J,WHI,POLICE OFFICER,259804\n'),  # noqa: E501
                ('officerbadgenumber', 'officer_id,star,cr_id\n1088.0,1986.0,259794\n56009.0,9331.0,259794\n,,259797\n50854.0,14380.0,259804\n50854.0,14380.0,259804\n50854.0,14380.0,259804\n50854.0,14380.0,259804\n39162.0,15738.0,259804\n50854.0,14380.0,259804\n'),  # noqa: E501
                ('policeunit', 'tags,unit_name,cr_id\n3.0,,259794\n3.0,,259794\n,,259797\n153.0,,259804\n153.0,,259804\n153.0,,259804\n153.0,,259804\n7.0,,259804\n153.0,,259804\n')  # noqa: E501
            ]
            actual_result = transformer.csv_to_entity_name_csv_tuples(file.read())
            assert actual_result == expected_result
