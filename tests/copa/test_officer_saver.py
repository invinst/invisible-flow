from datetime import datetime
from unittest.mock import patch
import pandas as pd
import numpy as np

from invisible_flow.copa.allegation_saver import AllegationSaver
from invisible_flow.copa.officer_saver import OfficerSaver
from invisible_flow.storage import LocalStorage
from invisible_flow.storage.storage_factory import StorageFactory
from invisible_flow.globals_factory import GlobalsFactory  # noqa: F401


class TestOfficerSaver:
    fake_new_rows = pd.DataFrame(np.array([["22222", "White", "F", "20-30", "5-10"],
                                           ["33333", "White", '', "20-30", "10-15"],
                                           ["44444", "White", '', "20-30", "15-20"]
                                           ]),
                                 columns=['allegation_id', 'race', 'gender', 'age', 'years_on_force'])

    fake_old_rows = pd.DataFrame(np.array([["99999", "White", "M", "40-49", "20-25"],
                                           ["77777", "White", '', "20-30", "5-10"]
                                           ]),
                                 columns=['allegation_id', 'race', 'gender', 'age', 'years_on_force'])

    @patch('invisible_flow.app.GlobalsFactory.get_current_datetime_utc', lambda: datetime(2019, 3, 25, 5, 30, 50, 0))
    def test_save_empty_officer_df_to_csv(self):
        empty_df = pd.DataFrame()
        with patch.object(StorageFactory, 'get_storage') as storage_mock, \
                patch.object(LocalStorage, 'store_byte_string') as store_byte_string_mock:
            storage_mock.return_value = LocalStorage()

            test_saver = AllegationSaver()
            test_saver.save_allegation_to_csv(empty_df, "filename")

            store_byte_string_mock.assert_called_with("filename", b"\n", f"COPA_SCRAPE-2019-03-25_05-30-50")

    @patch('invisible_flow.app.GlobalsFactory.get_current_datetime_utc', lambda: datetime(2019, 3, 25, 5, 30, 50, 0))
    def test_save_non_empty_officer_df_to_csv(self):
        with patch.object(StorageFactory, 'get_storage') as storage_mock, \
                patch.object(LocalStorage, 'store_byte_string') as store_byte_string_mock:
            storage_mock.return_value = LocalStorage()

            test_saver = OfficerSaver()
            test_saver.save_officer_to_csv(self.fake_old_rows, self.fake_new_rows)

            expected_new_officer_allegation_data = b"allegation_id,years_on_force\n22222,5-10\n33333,10-15\n44444,15-20\n"
            expected_old_officer_demographic_data = b"race,gender,age\nWhite,M,40-49\nWhite,,20-30\n"
            expected_old_officer_allegation_data = b"allegation_id,years_on_force\n99999,20-25\n77777,5-10\n"
            expected_new_officer_demographic_data = b"race,gender,age\nWhite,F,20-30\nWhite,,20-30\nWhite,,20-30\n"

            store_byte_string_mock.assert_called_with("old_officer_allegation_data.csv",
                                                      expected_old_officer_allegation_data,
                                                      f"COPA_SCRAPE-2019-03-25_05-30-50")

            store_byte_string_mock.assert_called_with("old_officer_demographic_data.csv",
                                                      expected_old_officer_demographic_data,
                                                      f"COPA_SCRAPE-2019-03-25_05-30-50")

            store_byte_string_mock.assert_called_with("new_officer_allegation_data.csv",
                                                      expected_new_officer_allegation_data,
                                                      f"COPA_SCRAPE-2019-03-25_05-30-50")

            store_byte_string_mock.assert_called_with("new_officer_demographic_data.csv",
                                                      expected_new_officer_demographic_data,
                                                      f"COPA_SCRAPE-2019-03-25_05-30-50")

    def test_split_officer_allegation_should_split_into_allegation_and_demographics(self):
        test_saver = OfficerSaver()

        test_saver.split_officer_data(pd.DataFrame({
            "allegation_id": ["33333"],
            "race": ["White"],
            "sex": ["M"],
            "age": ["40-49"],
            "years_on_force": ["20-25"]
        }))
