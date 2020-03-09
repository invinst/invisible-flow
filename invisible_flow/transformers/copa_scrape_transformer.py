import pandas as pd
from io import BytesIO


class CopaScrapeTransformer:

    def __init__(self):
        self.initial_data = pd.DataFrame()
        self.transformed_data = pd.DataFrame()
        self.non_transformable_data = pd.DataFrame()

    def transform(self, scraped_data: bytes):
        self.initial_data = pd.read_csv(BytesIO(scraped_data), encoding='utf-8', sep=",", dtype=str)

        crid = self.__transform_logno_to_crid()
        number_rows = self.__transform_officer_demographics_to_number_of_rows()

        self.transformed_data.insert(0, "cr_id", crid)
        self.transformed_data.insert(1, "number_of_officer_rows", number_rows)

    def __transform_logno_to_crid(self):
        transformed_logno = self.initial_data["log_no"].transform(lambda logno: logno)

        return transformed_logno

    def __transform_officer_demographics_to_number_of_rows(self):
        number_of_rows = self.initial_data["sex_of_involved_officers"].\
            transform(lambda sex: 0 if pd.isnull(sex) else len(sex.split('|')))

        return number_of_rows

    def get_transformed_data(self):
        return self.transformed_data

    def get_non_transformable_data(self):
        return self.non_transformable_data
