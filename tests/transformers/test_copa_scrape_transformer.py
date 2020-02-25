import pandas as pd

from invisible_flow.transformers.copa_scrape_transformer import CopaScrapeTransformer
from tests.helpers.testing_data import transformed_data as expected_transformed_data


scraped_data_csv = b'"log_no"\n"1008899"\n"1087378"\n"1087387"\n"1087308"\n"1008913"'

scraped_data_csv_with_demographics = b'"log_no","beat","race_of_involved_officers","sex_of_involved_officers",'\
                                     + b'"age_of_involved_officers","years_on_force_of_officers"\n"1008899","433",,,,'\
                                     + b'"\n1087378",,,,,\n"1087387","332","African American / Black | White","Male | '\
                                       b'Male","30-39 | 20-29","5-9 | 0-4"\n"1087308",,,,,\n"1008913","2512",,,,\n'


class TestCopaTransformer:

    def test_copa_transform(self):
        transformer = CopaScrapeTransformer()
        transformer.transform(scraped_data_csv)
        transformed_data = transformer.get_transformed_data()
        pd.testing.assert_frame_equal(transformed_data, expected_transformed_data)

#    def test_transform_officer_demographics_to_number_of_rows(self):
