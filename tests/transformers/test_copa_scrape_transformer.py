import pandas as pd
import pytest

from invisible_flow.transformers.copa_scrape_transformer import CopaScrapeTransformer

scraped_data_csv_with_demographics = b'"log_no","beat","race_of_involved_officers","sex_of_involved_officers",' \
                                     + b'"age_of_involved_officers","years_on_force_of_officers"\n' \
                                     + b'"1008899","Unknown","White","Male","40-49","0-4"' \
                                     + b'\n"1087378","0111","Black or African American","Male","40-49","0-4"' \
                                     + b'\n"1087387","0111","White | White","Female | Female",' \
                                       b'"40-49 | 40-49","0-4 | 0-4"' \
                                     + b'\n"1087308",,"Hispanic, Latino, or Spanish Origin","Male","40-49","0-4"' \
                                     + b'\n"1008913",,"Hispanic, Latino, or Spanish Origin","Female","40-49","0-4"\n'

scraped_data_csv_empty_demographic = b'"log_no","beat","race_of_involved_officers","sex_of_involved_officers",' \
                                     + b'"age_of_involved_officers","years_on_force_of_officers"' \
                                     + b'\n"1008899","433",,,,'

scraped_data_csv_single_demographic_entry = b'"log_no","beat","race_of_involved_officers","sex_of_involved_officers",' \
                                            + b'"age_of_involved_officers","years_on_force_of_officers"' \
                                            + b'\n"1008899","433","White","Male","30-39","0-4"'

scraped_data_csv_multiple_demographics = b'"log_no","beat","race_of_involved_officers","sex_of_involved_officers",' \
                                         + b'"age_of_involved_officers","years_on_force_of_officers"' \
                                         + b'\n"1008899","433","White | Black or African American","Male | Unknown",' \
                                           b'"30-39 | 20-29","0-4 | 0-4"'

scraped_data_with_all_races = pd.DataFrame({
    'log_no': ["1008899"],
    'beat': ['0111'],
    'race_of_involved_officers': ['White | Black or African American | Hispanic, Latino, or Spanish Origin | Unknown '
                                  '| Asian or Pacific Islander | Middle Eastern or North African | American Indian or '
                                  'Alaska Native'],
    'sex_of_involved_officers': ['Male | Male | Non-Binary/Third Gender | Female | Male | Female | Unknown'],
    'years_on_force_of_officers': ["0-4 | 0-4 | 0-4 | 0-4 | 0-4 | 0-4 | 0-4"],
    'age_of_involved_officers': ["40-49 | 40-49 | 40-49 | 40-49 | 40-49 | 40-49 | 40-49"]
})


class TestCopaTransformer:

    def test_copa_transform_with_demographics(self):
        transformer = CopaScrapeTransformer()
        transformer.transform(scraped_data_csv_with_demographics)
        transformed_data = transformer.get_transformed_data()
        pd.testing.assert_frame_equal(transformed_data, pd.DataFrame(
            {
                'cr_id': ["1008899", "1087378", "1087387", "1087308", "1008913"],
                'number_of_officer_rows': [1, 1, 2, 1, 1],
                'beat_id': [0, 111, 111, 0, 0],
                'officer_race': [["White"], ["Black"], ["White", "White"],
                                 ["Hispanic"], ["Hispanic"]],
                'officer_gender': [['M'], ['M'], ['F', 'F'], ['M'], ['F']],
                'officer_age': [["40-49"], ["40-49"], ["40-49", "40-49"], ["40-49"], ["40-49"]],
                'officer_years_on_force': [["0-4"], ["0-4"], ["0-4", "0-4"], ["0-4"], ["0-4"]]
            }))

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
            'officer_age': [[]],
            'officer_years_on_force': [[]]
        }))

    def test__transform_officer_should_return_one_row_when_demographic_string_has_one_officer(self):
        transformer = CopaScrapeTransformer()
        transformer.transform(scraped_data_csv_single_demographic_entry)
        transformed_data = transformer.get_transformed_data()
        pd.testing.assert_frame_equal(transformed_data, pd.DataFrame({
            'cr_id': ["1008899"],
            'number_of_officer_rows': [1],
            'beat_id': [433],
            'officer_race': [["White"]],
            'officer_gender': [["M"]],
            'officer_age': [["30-39"]],
            'officer_years_on_force': [["0-4"]]
        }))

    def test__transform_officer_should_return_multiple_rows_when_demographic_string_has_multiple_officer(self):
        transformer = CopaScrapeTransformer()
        transformer.transform(scraped_data_csv_multiple_demographics)
        transformed_data = transformer.get_transformed_data()
        pd.testing.assert_frame_equal(transformed_data, pd.DataFrame({
            'cr_id': ["1008899"],
            'number_of_officer_rows': [2],
            'beat_id': [433],
            'officer_race': [["White", "Black"]],
            'officer_gender': [["M", "U"]],
            'officer_age': [["30-39", "20-29"]],
            'officer_years_on_force': [["0-4", "0-4"]]
        }))

    def test__transform_officer_race_demographics(self):
        transformer = CopaScrapeTransformer()
        transformer.transform(scraped_data_with_all_races.to_csv(index=False).encode('utf-8'))
        transformed_data = transformer.get_transformed_data()
        pd.testing.assert_frame_equal(transformed_data, pd.DataFrame({
            'cr_id': ["1008899"],
            'number_of_officer_rows': [7],
            'beat_id': [111],
            'officer_race': [['White', 'Black', 'Hispanic', 'Unknown',
                              'Asian/Pacific', "Middle Eastern or North African",
                              "Native American/Alaskan Native"]],
            'officer_gender': [['M', 'M', 'N', 'F', 'M', 'F', "U"]],
            'officer_age': [["40-49", "40-49", "40-49", "40-49", "40-49", "40-49", "40-49"]],
            'officer_years_on_force': [["0-4", "0-4", "0-4", "0-4", "0-4", "0-4", "0-4"]]
        }), check_dtype=False)
