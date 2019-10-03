import os

from typing import List, Dict

from invisible_flow.globals_factory import GlobalsFactory
from invisible_flow.storage.storage_factory import StorageFactory
from invisible_flow.transformers.transformer_base import TransformerBase
from invisible_flow.api.copa_scrape import CopaScrape


class CopaScrapeTransformer(TransformerBase):

    def __init__(self):
        self.storage = StorageFactory.get_storage()
        self.scraper = CopaScrape()
        self.current_date = GlobalsFactory.get_current_datetime_utc().isoformat(sep='_').replace(':', '-')

    def save_scraped_data(self):
        scraper = CopaScrape()
        response = scraper.scrape_data_csv()
        csv = response.content
        if response.status_code == 200:
            self.storage.store_string('initial_data.csv', csv, f'Scrape-{self.current_date}/initial_data')
            self.create_and_save_metadata('initial_data')
        else:
            error_to_write = str(response.status_code) + "\n" + response.text
            self.storage.store_string('transform_error.csv', error_to_write, f'Scrape-{self.current_date}/errors')

    def split(self) -> Dict[str, List]:
        # on error needs to call store_string with a string describing the error
        scraper = CopaScrape()
        response = scraper.scrape_copa_csv()
        if response.status_code == 200:
            return {
                'copa': response.content,
                'no_copa': self.scraper.scrape_not_copa_csv()
            }
        else:
            error_to_write = str(response.status_code) + "\n" + response.text
            self.storage.store_string('transform_error.csv', error_to_write, f'Scrape-{self.current_date}/errors')
            return {}

    def upload_to_gcs(self, conversion_results: Dict):
        for result in conversion_results:
            filename = "copa" if result == "copa" else "other-assignment"
            self.storage.store_string(
                f'{filename}.csv',
                conversion_results[result],
                f'Scrape-{self.current_date}/cleaned'
            )

    def transform(self, response_type: str, file_content: str):
        self.save_scraped_data()
        blob = self.storage.get('copa.csv', f'Scrape-{self.current_date}/cleaned/')
        if blob is None:
            self.upload_to_gcs(self.split())

        allegation_rows = self.scraper.scrape_copa_ready_for_entity()
        self.storage.store_string('copa.csv', allegation_rows, f'Scrape-{self.current_date}/transformed')

        misc_data = self.scraper.scrape_copa_not_in_entity()
        self.storage.store_string('misc-data.csv', misc_data, f'Scrape-{self.current_date}/transformed')
        self.create_and_save_metadata('transformed')

    def create_and_save_metadata(self, data_folder: str):
        try:
            package_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
            commit = open(os.path.join(package_directory, 'commit')).read().strip()
        except FileNotFoundError:
            commit = 'No file found'
        metadata = b'{"git": "' + bytes(commit, encoding='UTF-8') + b'", "source": "SCRAPER/copa"}'
        self.storage.store_string_with_type(
            'metadata.json',
            metadata,
            f'Scrape-{self.current_date}/{data_folder}',
            'application/json'
        )
