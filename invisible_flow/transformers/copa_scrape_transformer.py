from typing import Tuple, List, Dict


from invisible_flow.transformers.transformer_base import TransformerBase
from invisible_flow.api.copa_scrape import CopaScrape


class CopaScrapeTransformer(TransformerBase):

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

    def transform(self, response_type: str, file_content: str) -> List[Tuple[str, str]]:
        pass
