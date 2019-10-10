import os
from datetime import datetime
from unittest import mock

from unittest.mock import call, patch
import pytest

from invisible_flow.constants import SCRAPE_URL
from invisible_flow.globals_factory import GlobalsFactory
from invisible_flow.storage import LocalStorage
from invisible_flow.transformers.copa_scrape_transformer import CopaScrapeTransformer

from tests.helpers.if_test_base import IFTestBase

response_code = 200


def mocked_requests_get(**kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code, content):
            self.json_data = json_data
            self.status_code = status_code
            self.content = content
            self.message = "DANGER DANGER"
            self.text = "response text property value"

        def json(self):
            return self.json_data

    if kwargs == {"url": SCRAPE_URL + ".csv"}:
        return MockResponse({"key1": "value1"}, response_code, b"bubbles")
    elif kwargs == {"url": SCRAPE_URL + ".json"}:
        return MockResponse({"key1": "value1"}, response_code, b"bubbles")
    elif kwargs == {"url": SCRAPE_URL + ".csv?$where=assignment=\"COPA\""}:
        return MockResponse({"key1": "value1"}, response_code, b"bubbles")
    elif kwargs == {"url": SCRAPE_URL + ".csv?$where=assignment!=\"COPA\""}:
        return MockResponse({"key1": "value1"}, response_code, b"bubbles")
    elif kwargs == {"url": SCRAPE_URL + ".csv?$select=log_no,complaint_date,beat&$where=assignment=\"COPA\""}:
        return MockResponse({"key1": "value1"}, response_code, b"bubbles")
    elif kwargs == {"url": SCRAPE_URL + ".csv?$select=log_no,assignment,case_type,current_status,"
                                        "current_category,finding_code,police_shooting,race_of_complainants,"
                                        "sex_of_complainants,age_of_complainants,"
                                        "race_of_involved_officers,sex_of_involved_officers,age_of_involved_officers,"
                                        "years_on_force_of_officers,complaint_hour,complaint_day,complaint_month&"
                                        "$where=assignment=\"COPA\""}:
        return MockResponse({"key1": "value1"}, response_code, b"bubbles")

    return MockResponse(None, 404, None)


@mock.patch('requests.get', side_effect=mocked_requests_get)
class TestCopaScrapeTransformer(IFTestBase):
    @pytest.fixture(
        autouse=True,
        params=[200, 404]
    )
    def default_fixture(self, request):
        global response_code
        response_code = request.param
        with patch('invisible_flow.app.StorageFactory.get_storage') as get_storage_mock:
            get_storage_mock.return_value = LocalStorage()
            self.transformer = CopaScrapeTransformer()

    @patch('invisible_flow.app.GlobalsFactory.get_current_datetime_utc', lambda: datetime(2019, 3, 25, 5, 30, 50, 0))
    def test_save_scraped_data_with_all_response_codes(self, get_mock):
        if response_code == 200:
            filename = "initial_data.csv"
            pathname = "initial_data"
        else:
            filename = "initial_data_error.csv"
            pathname = "errors"
        with patch('invisible_flow.app.StorageFactory.get_storage') as get_storage_mock:
            with patch('invisible_flow.storage.LocalStorage.store_string') as store_string_mock:
                get_storage_mock.return_value = LocalStorage()
                CopaScrapeTransformer().save_scraped_data()
                self.current_date = GlobalsFactory.get_current_datetime_utc().isoformat(sep='_').replace(':', '-')
                calls = [
                    call(filename, mock.ANY, f'Scrape-{self.current_date}/{pathname}')
                ]
                store_string_mock.assert_has_calls(calls)

    @patch('invisible_flow.app.GlobalsFactory.get_current_datetime_utc', lambda: datetime(2019, 3, 25, 5, 30, 50, 0))
    def test_copa_data_handling(self, get_mock):
        with patch('invisible_flow.app.StorageFactory.get_storage') as get_storage_mock:
            get_storage_mock.return_value = LocalStorage()
            transformer = CopaScrapeTransformer()
            copa_data = transformer.copa_data_handling()
            self.current_date = GlobalsFactory.get_current_datetime_utc().isoformat(sep='_').replace(':', '-')
            if response_code == 200:
                assert copa_data == b"bubbles"
            else:
                assert len(transformer.error_log) > 0

    def test_not_copa_data_handling(self, get_mock):
        with patch('invisible_flow.app.StorageFactory.get_storage') as get_storage_mock:
            get_storage_mock.return_value = LocalStorage()
            transformer = CopaScrapeTransformer()
            not_copa_data = transformer.not_copa_data_handling()
            self.current_date = GlobalsFactory.get_current_datetime_utc().isoformat(sep='_').replace(':', '-')
            if response_code == 200:
                assert not_copa_data == b"bubbles"
            else:
                assert len(transformer.error_log) > 0

    @patch('invisible_flow.app.GlobalsFactory.get_current_datetime_utc', lambda: datetime(2019, 3, 25, 5, 30, 50, 0))
    def test_error_handling(self, get_mock):
        with patch('invisible_flow.app.StorageFactory.get_storage') as get_storage_mock:
            with patch('invisible_flow.storage.LocalStorage.store_string') as store_string_mock:
                get_storage_mock.return_value = LocalStorage()

                filename = "transform_error.csv"
                pathname = "errors"

                self.current_date = GlobalsFactory.get_current_datetime_utc().isoformat(sep='_').replace(':', '-')

                copaScrapeTransformer = CopaScrapeTransformer()
                copaScrapeTransformer.store_errors()

                calls = [
                    call(filename, mock.ANY, f'Scrape-{self.current_date}/{pathname}')
                ]

                if len(copaScrapeTransformer.error_log) != 0:
                    store_string_mock.assert_has_calls(calls)
                else:
                    store_string_mock.assert_not_called()

    def test_data_retrieval_wrapper(self, get_mock):
        with patch('invisible_flow.app.StorageFactory.get_storage') as get_storage_mock:
            with patch('invisible_flow.transformers.CopaScrapeTransformer.copa_data_handling') as\
                    copa_data_handling_mock:
                with patch('invisible_flow.transformers.CopaScrapeTransformer.not_copa_data_handling') as \
                        not_copa_data_handling_mock:
                    with patch('invisible_flow.transformers.CopaScrapeTransformer.store_errors') as store_errors_mock:
                        get_storage_mock.return_value = LocalStorage()
                        transformer = CopaScrapeTransformer()
                        data_retrieved = transformer.data_retrieval_wrapper()

                        if response_code == 200:
                            len(data_retrieved) == 2
                            len(transformer.error_log) == 0

                        if response_code == 404:
                            len(data_retrieved) == 0
                            len(transformer.error_log) == 2

                        copa_data_handling_mock.assert_called()
                        not_copa_data_handling_mock.assert_called()
                        store_errors_mock.assert_called()

    def test_upload_to_gcs(self, get_mock):
        copa_split_csv = os.path.join(IFTestBase.resource_directory, 'copa_scraped_split.csv')
        no_copa_split_csv = os.path.join(IFTestBase.resource_directory, 'no_copa_scraped_split.csv')
        mock_converted_output = {"copa": open(copa_split_csv).read(), "no_copa": open(no_copa_split_csv).read()}
        with patch('invisible_flow.app.StorageFactory.get_storage') as get_storage_mock:
            with patch.object(LocalStorage, 'store_string') as mock:
                get_storage_mock.return_value = LocalStorage()
                self.transformer.upload_to_gcs(mock_converted_output)
        mock.assert_called()

    @patch('invisible_flow.app.GlobalsFactory.get_current_datetime_utc', lambda: datetime(2019, 3, 25, 5, 30, 50, 0))
    def test_transform(self, get_mock):
        with patch('invisible_flow.app.StorageFactory.get_storage') as get_storage_mock:
            with patch.object(LocalStorage, 'store_string') as store_string_mock:
                with patch('invisible_flow.api.CopaScrape.scrape_copa_ready_for_entity') as mock_scrape_entity:
                    with patch('invisible_flow.api.CopaScrape.scrape_copa_not_in_entity') as mock_scrape_misc:
                        with patch.object(CopaScrapeTransformer, 'save_scraped_data'):
                            with patch.object(CopaScrapeTransformer, 'upload_to_gcs'):
                                get_storage_mock.return_value = LocalStorage()
                                mock_scrape_entity.return_value = b'some content'
                                mock_scrape_misc.return_value = b'some content'
                                CopaScrapeTransformer().transform(None, None)
        self.current_date = GlobalsFactory.get_current_datetime_utc().isoformat(sep='_').replace(':', '-')
        calls = [
            call("copa.csv", b"some content", f'Scrape-{self.current_date}/transformed'),
            call("misc-data.csv", b"some content", f'Scrape-{self.current_date}/transformed')
        ]
        store_string_mock.assert_has_calls(calls)
