import pandas as pd
import numpy as np

from invisible_flow.transformers.allegation_transformer import AllegationTransformer
from pandas.testing import assert_series_equal


class TestAllegationTransformer():

    def test_transform_beat_id_should_give_first_valid_beat_id_or_empty(self):
        fake_new_rows = pd.DataFrame({
            "log_no": ["33333333", "1111111", "999999", "100000", "100007",
                       "1101010", "1101110", "201398", "021938", "32093"],
            "beat": ["111", "112 | 113", "123123 | 114", "121", "Unknown", "0", "", 10, 111, np.nan]
        })
        expected_beat_ids = pd.Series(["111", "112", "114", "121", "", "", "", "", "111", ""], name="beat")

        test_transformer = AllegationTransformer()
        transformed_scrape_data = test_transformer.transform_beat_id(fake_new_rows)
        assert_series_equal(transformed_scrape_data["beat"], expected_beat_ids)

    def test_transformer_should_change_column_names_to_match_db(self):
        fake_new_rows = pd.DataFrame({
            "log_no": ["11111"],
            "beat": ["111"]
        })

        test_transformer = AllegationTransformer()
        transformed_scrape_data = test_transformer.transform(fake_new_rows)

        assert("cr_id" in transformed_scrape_data.columns)
        assert("beat_id" in transformed_scrape_data.columns)
        assert("log_no" not in transformed_scrape_data.columns)
        assert("beat" not in transformed_scrape_data.columns)
