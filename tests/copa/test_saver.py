import pytest
from datetime import datetime
from unittest.mock import patch

from invisible_flow.copa.saver import Saver
from invisible_flow.storage import LocalStorage
from invisible_flow.storage.storage_factory import StorageFactory
from tests.helpers.testing_data import transformed_data


class TestSaver:

    @pytest.fixture
    def get_data(self):
        data = []
        for row in transformed_data.itertuples():
            data.append(transformed_data.iloc[row[0]])

        yield data

    @patch('invisible_flow.app.GlobalsFactory.get_current_datetime_utc', lambda: datetime(2019, 3, 25, 5, 30, 50, 0))
    def test_save_empty_list_to_csv(self):
        with patch.object(StorageFactory, 'get_storage') as storage_mock, \
                patch.object(LocalStorage, 'store_byte_string') as store_byte_string_mock:

            storage_mock.return_value = LocalStorage()

            test_saver = Saver()
            test_saver.save_to_csv([], "filename")

            store_byte_string_mock.assert_called_with("filename", b"", f"COPA_SCRAPE-2019-03-25_05-30-50")

    @patch('invisible_flow.app.GlobalsFactory.get_current_datetime_utc', lambda: datetime(2019, 3, 25, 5, 30, 50, 0))
    def test_save_non_empty_list_to_csv(self, get_data):
        with patch.object(StorageFactory, 'get_storage') as storage_mock, \
                patch.object(LocalStorage, 'store_byte_string') as store_byte_string_mock:

            storage_mock.return_value = LocalStorage()

            test_saver = Saver()
            test_saver.save_to_csv(get_data, "filename")

            store_byte_string_mock.assert_called_with("filename",
                                                      b"cr_id\n1008899\n1087378\n1087387\n1087308\n1008913\n",
                                                      f"COPA_SCRAPE-2019-03-25_05-30-50")
