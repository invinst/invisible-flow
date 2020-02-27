import pandas as pd

from invisible_flow.transformers.copa_scrape_transformer import CopaScrapeTransformer
from tests.helpers.testing_data import transformed_data as expected_transformed_data


scraped_data_csv = b'"log_no","beat"\n' \
                   b'"1008899","433"\n' \
                   b'"1087378","511"\n' \
                   b'"1087387","332"\n' \
                   b'"1087308","1712"\n' \
                   b'"1008913","2512|933"'


class TestCopaTransformer:

    def test_copa_transform(self):
        transformer = CopaScrapeTransformer()
        transformer.transform(scraped_data_csv)
        transformed_data = transformer.get_transformed_data()
        pd.testing.assert_frame_equal(transformed_data, expected_transformed_data)
