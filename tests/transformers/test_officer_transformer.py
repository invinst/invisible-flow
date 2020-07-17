import pandas as pd
import numpy as np
import pytest

from invisible_flow.transformers.allegation_transformer import AllegationTransformer
from pandas.testing import assert_series_equal

from invisible_flow.transformers.officer_transformer import OfficerTransformer


class TestAllegationTransformer():

    def test_transformer_should_change_column_names_to_match_db(self):
        fake_new_rows = pd.DataFrame({
            "log_no": ["11111"],
            "race_of_involved_officer": ["White"],
            "sex_of_involved_officer": ["M"],
            "age_of_involved_officer": ["40-49"],
            "years_on_force_of_involved_officer": ["20-25"]
        })

        test_transformer = OfficerTransformer()
        transformed_scrape_data = test_transformer.transform_officer_column_names(fake_new_rows)

        assert("allegation_id" in transformed_scrape_data.columns)
        assert("race" in transformed_scrape_data.columns)
        assert ("gender" in transformed_scrape_data.columns)
        assert ("age" in transformed_scrape_data.columns)
        assert ("years_on_force" in transformed_scrape_data.columns)

        assert("log_no" not in transformed_scrape_data.columns)
        assert("age_of_involved_officer" not in transformed_scrape_data.columns)
        assert ("race_of_involved_officer" not in transformed_scrape_data.columns)
        assert ("sex_of_involved_officer" not in transformed_scrape_data.columns)
        assert ("years_on_force_of_involved_officer" not in transformed_scrape_data.columns)

