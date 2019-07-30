import pandas as pd
import os

from invisible_flow.entities.data_investigator import Investigator
from invisible_flow.transformers.investigator_transformer import InvestigatorTransformer


class TestInvestigatorTransformer:
    expected_output_path = os.path.join(
        '.', 'tests', 'resources', 'investigator_transform_output.csv')
    investigator_csv_path = os.path.join(
        '.', 'tests', 'resources', 'sample_investigator_request.csv')

    def test_transform_investigator_csv_to_investigator_entity_list(self):
        with open(self.investigator_csv_path) as file:
            actual = InvestigatorTransformer.transform_investigator_csv_to_entity_list(file.read())
            expected = [Investigator(last_name='DALKIN',
                                     first_name='ANDREW',
                                     middle_initial='',
                                     gender='M',
                                     race="WHI",
                                     appointed_date='17-MAY-17',
                                     officer_id=0)]
        assert actual == expected

    def test_transform_investigator_entity_to_investigator_df(self):
        investigator_list = [Investigator(last_name='DALKIN',
                                          first_name='ANDREW',
                                          middle_initial='',
                                          gender='M',
                                          race="WHI",
                                          appointed_date='17-MAY-17',
                                          officer_id=0),
                             Investigator(last_name='CROSS',
                                          first_name='FREDERICK',
                                          middle_initial='',
                                          gender='M',
                                          race="BLA",
                                          appointed_date='5-MAY-10',
                                          officer_id=0)]
        column_names = ['last_name', 'first_name', 'middle_initial',
                        'gender', 'race', 'appointed_date', 'officer_id']
        source_arrays = [['DALKIN', 'ANDREW', '', 'M', 'WHI', '17-MAY-17',
                          0], ['CROSS', 'FREDERICK', '', 'M', 'BLA', '5-MAY-10', 0]]
        expected = pd.DataFrame(source_arrays, columns=column_names)
        actual = InvestigatorTransformer.transform_investigator_entities_to_df(
            investigator_list)
        assert expected.equals(actual)

    def test_transform_investigator_csv_to_investigator_csv(self):
        with open(self.investigator_csv_path) as input_file, \
                open(self.expected_output_path) as expected_output_file:
            initial_investigator_content = input_file.read()
            actual_output = InvestigatorTransformer.transform_investigator_csv_to_investigator_csv(
                initial_investigator_content)
            expected_output = expected_output_file.read()
            assert actual_output == expected_output

    def test_transform_returns_filename_and_contents(self):
        with open(self.investigator_csv_path) as input_file, \
                open(self.expected_output_path) as expected_output_file:
            initial_investigator_content = input_file.read()

            expected = expected_output_file.read()
            actual = InvestigatorTransformer().transform(None, initial_investigator_content)
            assert actual == expected
