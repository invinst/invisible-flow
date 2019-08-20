import pandas as pd

from typing import List, Dict

from invisible_flow.storage.storage_factory import StorageFactory
from invisible_flow.transformers.transformer_base import TransformerBase
from invisible_flow.api.copa_scrape import CopaScrape


class CopaScrapeTransformer(TransformerBase):

    def __init__(self):
        self.storage = StorageFactory.get_storage()

    def split(self) -> Dict[str, List]:
        scraper = CopaScrape()
        data = scraper.scrape_data()
        copa = []
        no_copa = []
        for row in data:
            if row['assignment'] == 'COPA':
                copa.append(row)
            else:
                no_copa.append(row)
        return {'copa': copa, 'no_copa': no_copa}

    def convert_to_csv(self, split_results: Dict) -> Dict[str, str]:
        return {
            'copa':
                pd.read_json(split_results['copa'].to_json(orient='records'), orient='records').to_csv(index=False),
            'no_copa':
                pd.read_json(split_results['no_copa'].to_json(orient='records'), orient='records').to_csv(index=False)
        }

    def upload_to_gcs(self, conversion_results: Dict):
        for result in conversion_results:
            filename = "copa" if result == "copa" else "other-assignment"
            self.storage.store_string(f'{filename}.csv', conversion_results[result], f'cleaned')
        pass

    def transform(self, response_type: str, file_content: str):
        blob = self.storage.get('copa.csv', 'cleaned/')
        if blob is None:
            print("results not found")
        else:
            print("results found")
        pass
