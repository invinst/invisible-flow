import requests

from invisible_flow.constants import SCRAPE_URL


class CopaScrape:
    def scrape_data_json(self):
        url = SCRAPE_URL + ".json"
        resp = requests.get(url=url)
        return resp.json()

    def scrape_data_csv(self):
        url = SCRAPE_URL + ".csv"
        resp = requests.get(url=url)
        return resp.content
