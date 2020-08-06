from datetime import datetime
from unittest.mock import patch, call
import pandas as pd
import numpy as np

from invisible_flow.copa.allegation_saver import AllegationSaver
from invisible_flow.copa.officer_saver import OfficerSaver
from invisible_flow.storage import LocalStorage
from invisible_flow.storage.storage_factory import StorageFactory
from invisible_flow.globals_factory import GlobalsFactory  # noqa: F401


class TestOfficerSaver:
    fake_new_rows = pd.DataFrame(np.array([["22222", "White", "F", "20-30", "5-10"],
                                           ["33333", "White", 'U', "20-30", "10-15"],
                                           ["44444", "White", 'U', "20-30", "15-20"]
                                           ]),
                                 columns=['allegation_id', 'race', 'gender', 'age', 'years_on_force'])

    fake_old_rows = pd.DataFrame(np.array([["99999", "White", "M", "40-49", "20-25"],
                                           ["77777", "White", 'U', "20-30", "5-10"]
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

            expected_new_officer_allegation_data = b"allegation_id\n22222\n33333\n44444\n"
            expected_old_officer_demographic_data = b"age,gender,race,years_on_force\n40-49,M,White,20-25\n20-30,U,White,5-10\n"
            expected_old_officer_allegation_data = b"allegation_id\n99999\n77777\n"
            expected_new_officer_demographic_data = b"age,gender,race,years_on_force\n20-30,F,White,5-10\n20-30,U,White,10-15\n20-30,U,White,15-20\n"

            call1 = call("old_officer_allegation_data.csv",
                         expected_old_officer_allegation_data,
                         f"COPA_SCRAPE-2019-03-25_05-30-50")
            call2 = call("old_officer_demographic_data.csv",
                         expected_old_officer_demographic_data,
                         f"COPA_SCRAPE-2019-03-25_05-30-50")
            call3 = call("new_officer_allegation_data.csv",
                         expected_new_officer_allegation_data,
                         f"COPA_SCRAPE-2019-03-25_05-30-50")
            call4 = call("new_officer_demographic_data.csv",
                         expected_new_officer_demographic_data,
                         f"COPA_SCRAPE-2019-03-25_05-30-50")

            store_byte_string_mock.assert_has_calls([call1, call2, call3, call4], any_order=False)

    def test_split_officer_allegation_should_split_into_allegation_and_demographics(self):
        test_saver = OfficerSaver()

        test_saver.split_officer_data(pd.DataFrame({
            "allegation_id": ["33333"],
            "race": ["White"],
            "gender": ["M"],
            "age": ["40-49"],
            "years_on_force": ["20-25"]
        }))
