import requests

from invisible_flow.constants import SCRAPE_URL


class CopaScrape:
    def scrape_data(self):
        url = SCRAPE_URL
        resp = requests.get(url=url)
        return resp.json()
