import requests
import unittest
from unittest import mock

from mock import call

from invisible_flow.constants import SCRAPE_URL
from invisible_flow.storage import LocalStorage
from invisible_flow.transformers.copa_scrape_transformer import CopaScrapeTransformer


# This is the class we want to test
class MyGreatClass:
    def fetch_json(self, url):
        response = requests.get(url)
        return response.json()


# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code, content):
            self.json_data = json_data
            self.status_code = status_code
            self.content = content

        def json(self):
            return self.json_data
    if kwargs == {"url": SCRAPE_URL + ".csv"}:
        return MockResponse({"key1": "value1"}, 200, "bubbles")
    elif kwargs == {"url": "http://someotherurl.com/anothertest.json"}:
        return MockResponse({"key2": "value2"}, 200, "chubbles")

    return MockResponse(None, 404, None)


# Our test case class
class MyGreatClassTestCase(unittest.TestCase):

    # We patch 'requests.get' with our own method. The mock object is passed in to our test case method.
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_fetch(self, mock_get):
        # Assert requests.get calls
        with mock.patch('invisible_flow.app.StorageFactory.get_storage') as get_storage_mock:
            with mock.patch.object(LocalStorage, 'store_string') as choco:
                get_storage_mock.return_value = LocalStorage()
                CopaScrapeTransformer().save_scraped_data()
                calls = [
                    call(mock.ANY, "bubbles", mock.ANY),
                ]
                choco.assert_has_calls(calls)


if __name__ == '__main__':
    unittest.main()
