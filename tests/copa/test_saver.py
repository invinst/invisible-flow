import pandas as pd
import pytest
from datetime import datetime
from unittest.mock import patch

from pandas.util.testing import assert_frame_equal

from invisible_flow.copa.saver import Saver, strip_zeroes_from_beat_id, cast_col_to_int
from invisible_flow.storage import LocalStorage
from invisible_flow.storage.storage_factory import StorageFactory
from invisible_flow.globals_factory import GlobalsFactory
from tests.helpers.testing_data import expected_load_data


class TestSaver:

    @pytest.fixture
    # was using transformed_data initially, now uses expected_load_data; see: testing_data.py
    def get_data(self):
        data = []
        for row in expected_load_data.itertuples():
            data.append(expected_load_data.iloc[row[0]])  # row; 1 crid, 1 beat_id
        data_df = pd.DataFrame(data)
        yield data_df

    @patch('invisible_flow.app.GlobalsFactory.get_current_datetime_utc', lambda: datetime(2019, 3, 25, 5, 30, 50, 0))
    def test_save_empty_df_to_csv(self):
        empty_df = pd.DataFrame()  # test initially checked for "empty" list, no longer list, expected empty dataframe
        with patch.object(StorageFactory, 'get_storage') as storage_mock, \
                patch.object(LocalStorage, 'store_byte_string') as store_byte_string_mock:
            storage_mock.return_value = LocalStorage()

            test_saver = Saver()
            test_saver.save_to_csv(empty_df, "filename")

            store_byte_string_mock.assert_called_with("filename", b"\n", f"COPA_SCRAPE-2019-03-25_05-30-50")

    @patch('invisible_flow.app.GlobalsFactory.get_current_datetime_utc', lambda: datetime(2019, 3, 25, 5, 30, 50, 0))
    def test_save_non_empty_list_to_csv(self, get_data):
        with patch.object(StorageFactory, 'get_storage') as storage_mock, \
                patch.object(LocalStorage, 'store_byte_string') as store_byte_string_mock:
            storage_mock.return_value = LocalStorage()

            test_saver = Saver()
            test_saver.save_to_csv(get_data, "filename")

            '''
            line below used to only have crids being compared in list form, changed get_data to bring in dataframe
            instead of just single list and compared to expected which includes both crid/beat_id
            '''
            expected_file_contents = b"cr_id,beat_id\n1008899,433\n1087378,111\n1087387,111\n1087308,0\n1008913,0\n"

            store_byte_string_mock.assert_called_with("filename",
                                                      expected_file_contents,
                                                      f"COPA_SCRAPE-2019-03-25_05-30-50")

    @patch('invisible_flow.app.GlobalsFactory.get_current_datetime_utc', lambda: datetime(2019, 3, 25, 5, 30, 50, 0))
    def test_save_officer_unknown_table_to_csv(self, get_data):
        with patch.object(StorageFactory, 'get_storage') as storage_mock, \
                patch.object(LocalStorage, 'store_byte_string') as store_byte_string_mock:
            storage_mock.return_value = LocalStorage()

            officer_unknown_df = pd.DataFrame([
                {
                    "data_officerallegation_id": 1,
                    "age": '40-49',
                    "race": 'White',
                    "gender": 'M',
                    "years_on_force": '0-4'
                }
            ])

            test_saver = Saver()
            test_saver.save_to_csv(officer_unknown_df, "filename")

            expected_file_contents = officer_unknown_df.to_csv(index=False).encode('utf-8')

            store_byte_string_mock.assert_called_with("filename",
                                                      expected_file_contents,
                                                      f"COPA_SCRAPE-2019-03-25_05-30-50")

    def test_strip_zeroes_from_beat_id(self, get_data):
        df = pd.DataFrame([{"beat_id": 0}])
        actual_return_value = strip_zeroes_from_beat_id(df)
        assert_frame_equal(actual_return_value, pd.DataFrame([{"beat_id": ""}]))

    def test_cast_col_to_int(self, get_data):
        df = pd.DataFrame([{"data_officerallegation_id": float(0)}])
        actual_return_value = cast_col_to_int(df, "data_officerallegation_id")
        assert_frame_equal(actual_return_value, pd.DataFrame([{"data_officerallegation_id": int(0)}]))
