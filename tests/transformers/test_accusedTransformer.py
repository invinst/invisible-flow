import os

from invisible_flow.transformers.accused_transformer import AccusedTransformer

from tests.helpers.if_test_base import IFTestBase


class TestAccusedTransformer:

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
