import pandas as pd
import os

from invisible_flow.entities.data_investigator import Investigator
from invisible_flow.transformers.investigator_transformer import InvestigatorTransformer


class TestInvestigatorTransformer:
    expected_output_path = os.path.join(
        '.', 'tests', 'transformers', 'investigator_transform_output.csv')
    investigator_csv_path = os.path.join(
        '.', 'tests', 'resources', 'sample_investigator_request.csv')

    def test_transform_investigator_csv_to_investigator_entity_list(self):
        with open(self.investigator_csv_path) as file:
            actual = InvestigatorTransformer.transform_investigator_csv_to_entity_list(
                file.read())
            expected = [Investigator(last_name='DALKIN',
                                     first_name='ANDREW',
                                     middle_initial='',
                                     gender='M',
                                     race="WHI",
                                     appointed_date='17-MAY-17',
                                     officer_id=0)]
        assert actual == expected
