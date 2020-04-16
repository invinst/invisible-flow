import datetime
import os

import pandas as pd

from invisible_flow.transformers.complainant_transformer import ComplainantTransformer
from tests.helpers.if_test_base import IFTestBase


CURRENT_YEAR = datetime.datetime.now().year


class TestComplainantTransformer(IFTestBase):
    complainant_input_path = os.path.join(IFTestBase.resource_directory, 'complainant_test_single_row.csv')

    def test_change_birth_year_to_age(self):
        fake_df = pd.DataFrame([[1995]], columns=['BIRTH_YEAR'])

        new_df = fake_df.apply(ComplainantTransformer().change_birth_year_to_age, axis=1)

        expected_df = pd.DataFrame([[1995, CURRENT_YEAR - 1995]], columns=['BIRTH_YEAR', 'age'])

        pd.testing.assert_frame_equal(new_df, expected_df)

    def test_transform(self):
        with open(self.complainant_input_path) as input_file:
            input_str = input_file.read()
            expected_output = 'crid,race,gender,age\n1010785,BLACK,MALE,{}\n'.format(CURRENT_YEAR - 1962)

            actual_output = ComplainantTransformer().transform('', input_str)[0]
            assert actual_output[0] == 'complainants'
            assert actual_output[1] == expected_output
