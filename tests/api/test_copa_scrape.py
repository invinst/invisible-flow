from unittest import mock

import pytest

from invisible_flow.api.copa_scrape import scrape_data, scrape_allegation_data, scrape_officer_data, scrape_crids
from invisible_flow.constants import ALLEGATION_BASE_URL, OFFICER_BASE_URL


class MockResponse:
    def __init__(self, json_data, status_code, content):
        self.json_data = json_data
        self.status_code = status_code
        self.content = content


base_url = "https://data.cityofchicago.org/resource/mft5-nfa8.csv?$"
base_query = base_url + "query=SELECT%20log_no,beat,race_of_involved_officers,sex_of_involved_officers,"\
                       + "age_of_involved_officers,years_on_force_of_officers"
count_query = base_url + "query=SELECT%20count(log_no)"

allegation_query = ALLEGATION_BASE_URL + "query=SELECT%20log_no,beat"
allegation_count_query = ALLEGATION_BASE_URL + "query=SELECT%20count(log_no)"
officer_query = OFFICER_BASE_URL + "query=SELECT%20log_no,race_of_involved_officer,sex_of_involved_officer," \
                                   "age_of_involved_officer,years_on_force_of_involved_officer"
crid_query = ALLEGATION_BASE_URL + "query=SELECT%20log_no"


def mocked_rows_requests_get_failure(**kwargs):
    return MockResponse({"key1": "value1"}, 404, "rows failure")


def mocked_requests_get_failure(**kwargs):
    if kwargs['url'] == count_query:
        content = "count_log_no\n2000"
        return MockResponse({}, 200, content.encode('utf-8'))

    return MockResponse({"key1": "value1"}, 404, "bubbles failure")


def mocked_requests_get(**kwargs):
    if kwargs['url'] == base_query:
        return MockResponse({"key1": "value1"}, 200, "bubbles")
    elif kwargs['url'] == count_query:
        content = "count_log_no\n2000"
        return MockResponse({}, 200, content.encode('utf-8'))
    elif kwargs['url'] == base_query + "%20LIMIT%202000":
        return MockResponse({"key1": "value1"}, 200, "bubbles")

    return MockResponse({"key1": "value1"}, 404, "bubbles failure")


@mock.patch('requests.get', side_effect=mocked_requests_get)
def test_copa_scrape(self):
    should_be_bubbles = scrape_data()
    assert should_be_bubbles == "bubbles"


@mock.patch('requests.get', side_effect=mocked_requests_get_failure)
def test_copa_scrape_with_errors(self):
    with pytest.raises(ConnectionError):
        scrape_data()


@mock.patch('requests.get', side_effect=mocked_rows_requests_get_failure)
def test_copa_scrape_with_count_errors(self):
    with pytest.raises(ConnectionError):
        scrape_data()


def mocked_allegation_requests_get(**kwargs):
    if kwargs['url'] == allegation_query:
        return MockResponse({"key1": "value1"}, 200, "allegation")
    elif kwargs['url'] == count_query:
        content = "count_log_no\n2000"
        return MockResponse({}, 200, content.encode('utf-8'))
    elif kwargs['url'] == allegation_query + "%20LIMIT%202000":
        return MockResponse({"key1": "value1"}, 200, "allegation")

    return MockResponse({"key1": "value1"}, 404, "allegation failure")


def mocked_allegation_requests_get_failure(**kwargs):
    return MockResponse({"key1": "value1"}, 404, "allegation failure")


@mock.patch('requests.get', side_effect=mocked_allegation_requests_get)
def test_copa_allegation_scrape(self):
    should_be_allegation = scrape_allegation_data()
    assert should_be_allegation == "allegation"


@mock.patch('requests.get', side_effect=mocked_allegation_requests_get_failure)
def test_copa_allegation_scrape_with_errors(self):
    with pytest.raises(ConnectionError):
        scrape_allegation_data()


def mocked_officer_requests_get(**kwargs):
    if kwargs['url'] == officer_query:
        return MockResponse({"key1": "value1"}, 200, "officer")
    elif kwargs['url'] == count_query:
        content = "count_log_no\n2000"
        return MockResponse({}, 200, content.encode('utf-8'))
    elif kwargs['url'] == officer_query + "%20LIMIT%202000":
        return MockResponse({"key1": "value1"}, 200, "officer")

    return MockResponse({"key1": "value1"}, 404, "officer failure")


def mocked_officer_requests_get_failure(**kwargs):
    return MockResponse({"key1": "value1"}, 404, "officer failure")


@mock.patch('requests.get', side_effect=mocked_officer_requests_get)
def test_copa_officer_scrape(self):
    should_be_officer = scrape_officer_data()
    assert should_be_officer == "officer"


@mock.patch('requests.get', side_effect=mocked_officer_requests_get_failure)
def test_copa_officer_scrape_with_errors(self):
    with pytest.raises(ConnectionError):
        scrape_allegation_data()


def mocked_crid_requests_get(**kwargs):
    if kwargs['url'] == crid_query:
        return MockResponse({"key1": "value1"}, 200, "crid")
    elif kwargs['url'] == count_query:
        content = "count_log_no\n2000"
        return MockResponse({}, 200, content.encode('utf-8'))
    elif kwargs['url'] == crid_query + "%20LIMIT%202000":
        return MockResponse({"key1": "value1"}, 200, "crid")

    return MockResponse({"key1": "value1"}, 404, "crid failure")


def mocked_crid_requests_get_failure(**kwargs):
    return MockResponse({"key1": "value1"}, 404, "crid failure")


@mock.patch('requests.get', side_effect=mocked_crid_requests_get)
def test_copa_crid_scrape(self):
    should_be_crid = scrape_crids()
    assert should_be_crid == "crid"


@mock.patch('requests.get', side_effect=mocked_crid_requests_get_failure)
def test_copa_crid_scrape_with_errors(self):
    with pytest.raises(ConnectionError):
        scrape_crids()
