from unittest import mock

import pytest

from invisible_flow.api import CopaScrape
from invisible_flow.constants import SCRAPE_URL

response_code = 200


def mocked_requests_get(**kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code, content):
            self.json_data = json_data
            self.status_code = status_code
            self.content = content

        def json(self):
            return self.json_data
    if kwargs == {"url": SCRAPE_URL + ".csv"}:
        return MockResponse({"key1": "value1"}, response_code, "bubbles")
    elif kwargs == {"url": SCRAPE_URL + ".json"}:
        return MockResponse({"key1": "value1"}, response_code, "bubbles")
    elif kwargs == {"url": SCRAPE_URL + ".csv?$where=assignment=\"COPA\""}:
        return MockResponse({"key1": "value1"}, response_code, "bubbles")
    elif kwargs == {"url": SCRAPE_URL + ".csv?$where=assignment!=\"COPA\""}:
        return MockResponse({"key1": "value1"}, response_code, "bubbles")
    elif kwargs == {"url": SCRAPE_URL + ".csv?$select=log_no,complaint_date,beat&$where=assignment=\"COPA\""}:
        return MockResponse({"key1": "value1"}, response_code, "bubbles")
    elif kwargs == {"url": SCRAPE_URL + ".csv?$select=log_no,assignment,case_type,current_status,current_category,"
                    "finding_code,police_shooting,race_of_complainants,sex_of_complainants,age_of_complainants,"
                    "race_of_involved_officers,sex_of_involved_officers,age_of_involved_officers,"
                    "years_on_force_of_officers,complaint_hour,complaint_day,complaint_month&"
                    "$where=assignment=\"COPA\""}:
        return MockResponse({"key1": "value1"}, response_code, "bubbles")

    return MockResponse(None, 404, None)


@pytest.fixture(
    scope="class",
    autouse=True,
    params=[200, 404]
)
def default_fixture(request):
    global response_code
    response_code = request.param


@mock.patch('requests.get', side_effect=mocked_requests_get)
class TestCopaScrape():
    def test_scrape_data_csv(self, get_mock):
        should_be_bubbles = CopaScrape().scrape_data_csv()
        assert should_be_bubbles.content == "bubbles"

    def test_scrape_data_json(self, get_mock):
        should_be_json_data = CopaScrape().scrape_data_json()
        assert should_be_json_data == {"key1": "value1"}

    def test_scrape_copa_csv(self, get_mock):
        should_be_bubbles = CopaScrape().scrape_copa_csv().content
        assert should_be_bubbles == "bubbles"

    def test_scrape_not_copa_csv(self, get_mock):
        should_be_bubbles = CopaScrape().scrape_not_copa_csv()
        assert should_be_bubbles == "bubbles"

    def test_scrape_copa_ready_for_entity(self, get_mock):
        should_be_bubbles = CopaScrape().scrape_copa_ready_for_entity()
        assert should_be_bubbles == "bubbles"

    def test_scrape_copa_not_in_entity(self, get_mock):
        should_be_bubbles = CopaScrape().scrape_copa_not_in_entity()
        assert should_be_bubbles == "bubbles"
