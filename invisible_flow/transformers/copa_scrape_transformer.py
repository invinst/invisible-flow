import pandas as pd
from io import BytesIO


class CopaScrapeTransformer:

    def __init__(self):
        self.initial_data = pd.DataFrame()
        self.transformed_data = pd.DataFrame()
        self.non_transformable_data = pd.DataFrame()

    def transform(self, scraped_data: bytes):
        self.initial_data = pd.read_csv(BytesIO(scraped_data), encoding='utf-8', sep=",", dtype=str)

        crid = self.transform_logno_to_crid()
        # number_rows = self.transform_officer_demographics_to_number_of_rows()
        self.transformed_data.insert(0, "cr_id", crid)

    def transform_logno_to_crid(self):
        #  transformed_logno = self.initial_data["log_no"].transform(lambda logno: logno)
        return self.initial_data["log_no"]

    def transform_officer_demographics_to_number_of_rows(self):
        # number_of_rows = self.intial_data["sex_of_involved_officers"].transform(lambda sex_of_involved_officers:
        #                                                                       sex_of_involved_officers.split('|')
        #                                                                        .length())

        number_of_rows = 3
        return number_of_rows

    def get_transformed_data(self):
        return self.transformed_data

    def get_non_transformable_data(self):
        return self.non_transformable_data
