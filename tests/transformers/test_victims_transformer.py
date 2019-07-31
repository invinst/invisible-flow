import os

import pandas as pd

from invisible_flow.transformers.victim_transformer import VictimTransformer
from tests.helpers.if_test_base import IFTestBase


class TestVictimTransformer(IFTestBase):
    victim_input_path = os.path.join(IFTestBase.resource_directory, 'victim_test_single_row.csv')
    victim_output_path = os.path.join(IFTestBase.resource_directory, 'victim_test_converted_single_row.csv')

    def test_change_sex_to_one_letter_with_m(self):
        fake_df = pd.DataFrame([['MALE']], columns=['SEX'])

        new_df = fake_df.apply(VictimTransformer().change_sex_to_one_letter, axis='columns')

        expected_df = pd.DataFrame([['MALE', 'M']], columns=['SEX', 'gender'])

        pd.testing.assert_frame_equal(new_df, expected_df)

    def test_change_sex_to_one_letter_with_f(self):
        fake_df = pd.DataFrame([['FEMALE']], columns=['SEX'])

        new_df = fake_df.apply(VictimTransformer().change_sex_to_one_letter, axis='columns')

        expected_df = pd.DataFrame([['FEMALE', 'F']], columns=['SEX', 'gender'])

        pd.testing.assert_frame_equal(new_df, expected_df)

    def test_change_sex_to_one_letter_with_unkown_sex(self):
        fake_df = pd.DataFrame([['ZHIR']], columns=['SEX'])

        new_df = fake_df.apply(VictimTransformer().change_sex_to_one_letter, axis='columns')

        expected_df = pd.DataFrame([['ZHIR', '']], columns=['SEX', 'gender'])

        pd.testing.assert_frame_equal(new_df, expected_df)

    def test_transform(self):
        with open(self.victim_input_path) as input_file, \
                open(self.victim_output_path) as expected_output_file:
            input_str = input_file.read()
            expected_output = expected_output_file.read()

            actual_output = VictimTransformer().transform('victims', input_str)[0]
            assert actual_output[0] == 'victims'
            assert actual_output[1] == expected_output
