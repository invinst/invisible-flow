import pandas as pd

from invisible_flow.transformers.copa_scrape_transformer import CopaScrapeTransformer
from tests.helpers.testing_data import expected_transformed_data_with_beat_id as expected_transformed_data_with_rows

scraped_data_csv_with_demographics = b'"log_no","beat","race_of_involved_officers","sex_of_involved_officers",' \
                                    + b'"age_of_involved_officers","years_on_force_of_officers"\n' \
                                    + b'"1008899","433",,,,' \
                                    + b'\n"1087378","0111 | 0",,,,' \
                                    + b'\n"1087387","0 | 0111",' \
                                    + b'"African American / Black | White","Male | Male", "30-39 | 20-29","5-9 | 0-4"' \
                                    + b'\n"1087308","8888888",,,,' \
                                    + b'\n"1008913",,,,,\n'

scraped_data_csv_empty_demographic = b'"log_no","beat","race_of_involved_officers","sex_of_involved_officers",' \
                                    + b'"age_of_involved_officers","years_on_force_of_officers"' \
                                    + b'\n"1008899","433",,,,'

scraped_data_csv_single_demographic_entry = b'"log_no","beat","race_of_involved_officers","sex_of_involved_officers",' \
                                    + b'"age_of_involved_officers","years_on_force_of_officers"' \
                                    + b'\n"1008899","433",,,,'

scraped_data_csv_multiple_demographic_entry = b'"log_no","beat","race_of_involved_officers","sex_of_involved_officers",' \
                                    + b'"age_of_involved_officers","years_on_force_of_officers"' \
                                    + b'\n"1008899","433",,,,'

class TestCopaTransformer:

    def test_copa_transform_with_demographics(self):
        transformer = CopaScrapeTransformer()
        transformer.transform(scraped_data_csv_with_demographics)
        transformed_data = transformer.get_transformed_data()
        pd.testing.assert_frame_equal(transformed_data, expected_transformed_data_with_rows)

    @pytest.mark.focus
    def test__transform_officer_should_return_empty_list_when_demographic_string_is_empty(self):
        transformer = CopaScrapeTransformer()
        transformer.transform(scraped_data_csv_empty_demographic)
        transformed_data = transformer.get_transformed_data()
        pd.testing.assert_frame_equal(transformed_data, pd.DataFrame({
            'cr_id': ["1008899"],
            'number_of_officer_rows': [1],
            'beat_id': [433],
            'officer_race': [[]],
            'officer_gender': [[]],
            'officer_age': [[]]
        }))
