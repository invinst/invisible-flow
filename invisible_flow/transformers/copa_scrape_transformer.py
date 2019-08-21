from typing import List, Dict

from invisible_flow.storage.storage_factory import StorageFactory
from invisible_flow.transformers.transformer_base import TransformerBase
from invisible_flow.api.copa_scrape import CopaScrape


class CopaScrapeTransformer(TransformerBase):

    def __init__(self):
        self.storage = StorageFactory.get_storage()
        self.scraper = CopaScrape()

    def split(self) -> Dict[str, List]:
        return {
            'copa': self.scraper.scrape_copa_csv(),
            'no_copa': self.scraper.scrape_not_copa_csv()
        }

    def upload_to_gcs(self, conversion_results: Dict):
        for result in conversion_results:
            filename = "copa" if result == "copa" else "other-assignment"
            self.storage.store_string(f'{filename}.csv', conversion_results[result], f'cleaned')

    def transform(self, response_type: str, file_content: str):
        blob = self.storage.get('copa.csv', 'cleaned/')
        if blob is None:
            self.upload_to_gcs(self.split())

        allegation_rows = self.scraper.scrape_copa_ready_for_entity()
        self.storage.store_string('copa.csv', allegation_rows, 'transformed')

        misc_data = self.scraper.scrape_copa_not_in_entity()
        self.storage.store_string('misc-data.csv', misc_data, 'transformed')
