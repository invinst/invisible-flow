import pandas as pd

from invisible_flow.transformers.copa_scrape_transformer import CopaScrapeTransformer


scraped_data_csv = b'"log_no"\n"1008899"\n"1087378"\n"1087387"\n"1087308"\n"1008913"'

expected_transformed_data = pd.DataFrame(
    {
        'crid': ["1008899", "1087378", "1087387", "1087308", "1008913"]
    }
)


class TestCopaTransformer:

    def test_copa_transform(self):
        [transformed_data, transform_errors] = CopaScrapeTransformer().transform(scraped_data_csv)
        pd.testing.assert_frame_equal(transformed_data, expected_transformed_data)
