import pandas as pd
import numpy as np
import pytest

from invisible_flow.transformers.allegation_transformer import AllegationTransformer
from pandas.testing import assert_series_equal

from invisible_flow.transformers.officer_transformer import OfficerTransformer


class TestAllegationTransformer():
    @pytest.mark.officer_transformer_test
    def test_transformer_should_change_column_names_to_match_db(self):

        fake_new_rows = pd.DataFrame(np.array([["11111", "01/04/2019 02:48:23 PM", "No Finding", "White", "Male", "40-49", "20-25"],
                                               ["22222", "02/05/2020 02:45:23 AM", "Exonerated", "White", "Female", "20-30", "5-10"]
                                               ]),
                                     columns=['log_no', 'complaint_date', 'finding_code', 'race_of_involved_officer', 'sex_of_involved_officer',
                                              'age_of_involved_officer', 'years_on_force_of_involved_officer'])

        test_transformer = OfficerTransformer()
        fake_new_rows = test_transformer.transform_column_names(fake_new_rows)

        assert ("allegation_id" in fake_new_rows.columns)
        assert ("start_date" in fake_new_rows.columns)
        assert ("recc_finding" in fake_new_rows.columns)
        assert ("race" in fake_new_rows.columns)
        assert ("gender" in fake_new_rows.columns)
        assert ("age" in fake_new_rows.columns)
        assert ("years_on_force" in fake_new_rows.columns)

        assert ("log_no" not in fake_new_rows.columns)
        assert ("complaint_date" not in fake_new_rows.columns)
        assert ("finding_code" not in fake_new_rows.columns)
        assert ("age_of_involved_officer" not in fake_new_rows.columns)
        assert ("race_of_involved_officer" not in fake_new_rows.columns)
        assert ("sex_of_involved_officer" not in fake_new_rows.columns)
        assert ("years_on_force_of_involved_officer" not in fake_new_rows.columns)

    def test_officer_transformer_handles_bad_gender_values(self):
        fake_new_rows = pd.DataFrame(np.array([["11111", "White", 'Male', "40-49", "20-25"],
                                               ["22222", "White", 'Female', "20-30", "5-10"],
                                               ["22222", "White", 'Prefer not to say', "20-30", "5-10"],
                                               ["22222", "White", 'Non-Binary/Third Gender', "20-30", "5-10"],
                                               ["33333", "White", np.nan, "20-30", "5-10"]
                                               ], dtype=object),
                                     columns=['log_no', 'race_of_involved_officer', 'gender',
                                              'age_of_involved_officer', 'years_on_force_of_involved_officer'])

        test_transformer = OfficerTransformer()
        officer_demographic_data = test_transformer.transform_gender_data(fake_new_rows)
        assert (officer_demographic_data['gender'].str.contains('M|F|U|N|P', regex=True).all())

    def test_should_add_derived_columns(self):
        fake_new_rows = pd.DataFrame(np.array([["11111", "No Finding", "White", "Male", "40-49", "20-25"],
                                               ["22222", "Exonerated", "White", "Female", "20-30", "5-10"]
                                               ]),
                                     columns=['allegation_id', 'recc_finding', 'race', 'gender',
                                              'age', 'years_on_force'])
        test_transformer = OfficerTransformer()
        test_transformer.add_derived_columns(fake_new_rows)
        assert("final_finding" in fake_new_rows.columns)

    def test_race_transformer(self):
        fake_new_rows = pd.DataFrame(["White", "Unknown", "Black or African American", "Hispanic, Latino, or Spanish Origin",
                                      "Asian or Pacific Islander", "Middle Eastern or North African",
                                      "American Indian or Alaska Native", "blueberries", np.nan], columns=['race'])
        test_transformer = OfficerTransformer()
        test_transformer.transform_race_data(fake_new_rows)
        pd.testing.assert_frame_equal(fake_new_rows, pd.DataFrame(["White", "Unknown", "Black", "Hispanic", "Asian/Pacific",
                                                                   "Middle Eastern or North African",
                                                                   "Native American/Alaskan Native", "Unknown", "Unknown"], columns=['race']))