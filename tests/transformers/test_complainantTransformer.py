import os

import pandas as pd

from invisible_flow.transformers.complainant_transformer import ComplainantTransformer
from tests.helpers.if_test_base import IFTestBase


class TestComplainantTransformer(IFTestBase):
    complainant_input_path = os.path.join(IFTestBase.resource_directory, 'complainant_test_single_row.csv')
    complainant_output_path = os.path.join(IFTestBase.resource_directory, 'complainant_test_converted_single_row.csv')

    def test_change_birth_year_to_age(self):
        fake_df = pd.DataFrame([[1995]], columns=['BIRTH_YEAR'])

        new_df = fake_df.apply(ComplainantTransformer().change_birth_year_to_age, axis=1)

        expected_df = pd.DataFrame([[1995, 24]], columns=['BIRTH_YEAR', 'age'])

        pd.testing.assert_frame_equal(new_df, expected_df)

    def test_transform(self):
        with open(self.complainant_input_path) as input_file, \
                open(self.complainant_output_path) as expected_output_file:
            input_str = input_file.read()
            expected_output = expected_output_file.read()

            actual_output = ComplainantTransformer().transform('', input_str)
            assert actual_output == expected_output
