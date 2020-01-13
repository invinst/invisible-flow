import os

from typing import Dict

from invisible_flow.globals_factory import GlobalsFactory
from invisible_flow.storage.storage_factory import StorageFactory
from invisible_flow.transformers.transformer_base import TransformerBase
from invisible_flow.api.copa_scrape import CopaScrape


class CopaScrapeTransformer(TransformerBase):
    def __init__(self):
        self.storage = StorageFactory.get_storage()
        self.scraper = CopaScrape()
        self.current_date = GlobalsFactory.get_current_datetime_utc().isoformat(sep='_').replace(':', '-')
        self.error_log = "The page that you seek cannot be accessed at this time."

    def save_scraped_data(self):
        scraper = CopaScrape()
        response = scraper.scrape_data_csv()
        csv = response.content
        if response.status_code == 200:
            self.storage.store_byte_string('initial_data.csv', csv, f'Scrape-{self.current_date}/initial_data')
            self.create_and_save_metadata('initial_data')
        else:
            error_to_write = str(response.status_code) + "\n" + response.text
            self.storage.store_byte_string('initial_data_error.csv', error_to_write.encode('utf-8'),
                                           f'Scrape-{self.current_date}/errors')

    def store_errors(self):
        if len(self.error_log) != 0:
            self.storage.store_byte_string('transform_error.csv', self.error_log.encode('utf-8'),
                                           f'Scrape-{self.current_date}/errors')

    def copa_data_handling(self):
        scraper = CopaScrape()
        response = scraper.scrape_copa_csv()

        if response.status_code == 200:
            return response.content
        else:
            self.error_log += str(response.status_code) + "\n" + response.text

    def not_copa_data_handling(self):
        scraper = CopaScrape()
        response = scraper.scrape_not_copa_csv()

        if response.status_code == 200:
            return response.content
        else:
            self.error_log += str(response.status_code) + "\n" + response.text

    def data_retrieval_wrapper(self):
        data_retrieved = {}
        copa_data = self.copa_data_handling()
        non_copa_data = self.not_copa_data_handling()

        if copa_data is not None:
            data_retrieved['copa'] = copa_data

        if non_copa_data is not None:
            data_retrieved['non_copa'] = non_copa_data

        self.store_errors()
        return data_retrieved

    def upload_to_gcs(self, conversion_results: Dict[str, bytes]):
        for result in conversion_results:
            filename = "copa" if result == "copa" else "other-assignment"
            self.storage.store_byte_string(
                f'{filename}.csv',
                conversion_results[result],
                f'Scrape-{self.current_date}/cleaned'
            )

    # TODO: update/test for transform; what happens when either of the calls fail
    #  write error to storage
    def transform(self, response_type: str, file_content: str):
        split_data = self.data_retrieval_wrapper()
        self.save_scraped_data()
        blob = self.storage.get('copa.csv', f'Scrape-{self.current_date}/cleaned/')
        if blob is None:
            self.upload_to_gcs(split_data)

        allegation_rows = self.scraper.scrape_copa_ready_for_entity()
        self.storage.store_byte_string('copa.csv', allegation_rows, f'Scrape-{self.current_date}/transformed')

        misc_data = self.scraper.scrape_copa_not_in_entity()
        self.storage.store_byte_string('misc-data.csv', misc_data, f'Scrape-{self.current_date}/transformed')
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
