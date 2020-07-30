import pandas as pd
import numpy as np
import pytest

from invisible_flow.transformers.allegation_transformer import AllegationTransformer
from pandas.testing import assert_series_equal

from invisible_flow.transformers.officer_transformer import OfficerTransformer


class TestAllegationTransformer():
    @pytest.mark.officer_transformer_test
    def test_transformer_should_change_column_names_to_match_db(self):

        fake_new_rows = pd.DataFrame(np.array([["11111", "White", "Male", "40-49", "20-25"],
                                               ["22222", "White", "Female", "20-30", "5-10"]
                                               ]),
                                     columns=['log_no', 'race_of_involved_officer', 'sex_of_involved_officer',
                                              'age_of_involved_officer', 'years_on_force_of_involved_officer'])

        test_transformer = OfficerTransformer()
        transformed_scrape_data = test_transformer.transform(fake_new_rows)

        assert ("allegation_id" in transformed_scrape_data.columns)
        assert ("race" in transformed_scrape_data.columns)
        assert ("gender" in transformed_scrape_data.columns)
        assert ("age" in transformed_scrape_data.columns)
        assert ("years_on_force" in transformed_scrape_data.columns)

        assert ("log_no" not in transformed_scrape_data.columns)
        assert ("age_of_involved_officer" not in transformed_scrape_data.columns)
        assert ("race_of_involved_officer" not in transformed_scrape_data.columns)
        assert ("sex_of_involved_officer" not in transformed_scrape_data.columns)
        assert ("years_on_force_of_involved_officer" not in transformed_scrape_data.columns)



    def test_officer_transformer_handles_bad_gender_values(self):
        fake_new_rows = pd.DataFrame(np.array([["11111", "White", "Male", "40-49", "20-25"],
                                               ["22222", "White", "Female", "20-30", "5-10"],
                                               ["22222", "White", "Person", "20-30", "5-10"],
                                               ["22222", "White", None, "20-30", "5-10"],
                                               ["33333", "White", np.NaN, "20-30", "5-10"]
                                               ]),
                                     columns=['log_no', 'race_of_involved_officer', 'sex_of_involved_officer',
                                              'age_of_involved_officer', 'years_on_force_of_involved_officer'])

        test_transformer = OfficerTransformer()
        transformed_scrape_data = test_transformer.transform(fake_new_rows)
        assert (transformed_scrape_data['gender'].str.contains('M|F|U', regex=True).all())

