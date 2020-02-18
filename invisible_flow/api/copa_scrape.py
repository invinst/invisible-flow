import requests
import os

from invisible_flow.constants import SCRAPE_URL


def scrape_data():
    if os.environ.get("ENVIRONMENT") == 'local' or os.environ.get('ENVIRONMENT') == 'travis':
        num_rows = get_num_rows().replace("\"", "")
        url = SCRAPE_URL + ".csv?$query=SELECT%20log_no%20LIMIT%20" + num_rows
    else:
        url = SCRAPE_URL + ".csv?$select=log_no"

    response = requests.get(url=url)
    if response.status_code == 200:
        return response.content
    else:
        raise ConnectionError(response.content)


def get_num_rows():
    num_rows_query_url = SCRAPE_URL + ".csv?$query=SELECT%20count(log_no)"
    response = requests.get(url=num_rows_query_url)
    if response.status_code == 200:
        num_rows_csv = response.content
        num_rows = num_rows_csv.decode('utf-8').split('\n')[1]
        return num_rows
    else:
        raise ConnectionError(response.content)
