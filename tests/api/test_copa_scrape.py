from unittest import mock

import pytest

from invisible_flow.api.copa_scrape import scrape_data


class MockResponse:
    def __init__(self, json_data, status_code, content):
        self.json_data = json_data
        self.status_code = status_code
        self.content = content


def mocked_requests_get(**kwargs):
    return MockResponse({"key1": "value1"}, 200, "bubbles")


def mocked_requests_get_failure(**kwargs):
    return MockResponse({"key1": "value1"}, 404, "bubbles failure")


@mock.patch('requests.get', side_effect=mocked_requests_get)
def test_copa_scrape(self):
    should_be_bubbles = scrape_data()
    assert should_be_bubbles == "bubbles"


@mock.patch('requests.get', side_effect=mocked_requests_get_failure)
def test_copa_scrape_with_errors(self):
    with pytest.raises(ConnectionError):
        scrape_data()
