import requests

from invisible_flow.constants import SCRAPE_URL


def scrape_data():
    url = SCRAPE_URL + ".csv?$select=log_no"
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.content
    else:
        raise ConnectionError(response.content)
