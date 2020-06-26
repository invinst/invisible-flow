from datetime import datetime
from unittest.mock import patch
import pandas as pd

from invisible_flow.copa.allegation_saver import AllegationSaver
from invisible_flow.storage import LocalStorage
from invisible_flow.storage.storage_factory import StorageFactory
from invisible_flow.globals_factory import GlobalsFactory  # noqa: F401


class TestAllegationSaver:

    @patch('invisible_flow.app.GlobalsFactory.get_current_datetime_utc', lambda: datetime(2019, 3, 25, 5, 30, 50, 0))
    def test_save_empty_df_to_csv(self):
        empty_df = pd.DataFrame()
        with patch.object(StorageFactory, 'get_storage') as storage_mock, \
                patch.object(LocalStorage, 'store_byte_string') as store_byte_string_mock:
            storage_mock.return_value = LocalStorage()

            test_saver = AllegationSaver()
            test_saver.save_allegation_to_csv(empty_df, "filename")

            store_byte_string_mock.assert_called_with("filename", b"\n", f"COPA_SCRAPE-2019-03-25_05-30-50")

    @patch('invisible_flow.app.GlobalsFactory.get_current_datetime_utc', lambda: datetime(2019, 3, 25, 5, 30, 50, 0))
    def test_save_non_empty_list_to_csv(self):
        with patch.object(StorageFactory, 'get_storage') as storage_mock, \
                patch.object(LocalStorage, 'store_byte_string') as store_byte_string_mock:
            storage_mock.return_value = LocalStorage()

            test_saver = AllegationSaver()
            test_saver.save_allegation_to_csv(pd.DataFrame({
                "cr_id": ["33333333", "1111111", "999999", "100000", "100007"],
                "beat_id": ["111", "112", "114", "121", ""]
                }), "filename")

            expected_file_contents = b"cr_id,beat_id\n33333333,111\n1111111,112\n999999,114\n100000,121\n100007,\n"

            store_byte_string_mock.assert_called_with("filename",
                                                      expected_file_contents,
                                                      f"COPA_SCRAPE-2019-03-25_05-30-50")
