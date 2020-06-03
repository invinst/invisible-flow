import pandas as pd
from io import BytesIO
from invisible_flow.constants import VALID_BEATS


class CopaScrapeTransformer:

    def __init__(self):
        self.initial_data = pd.DataFrame()
        self.transformed_data = pd.DataFrame()
        self.non_transformable_data = pd.DataFrame()
        self.valid_beat_list = VALID_BEATS

    def transform(self, scraped_data: bytes):
        self.initial_data = pd.read_csv(BytesIO(scraped_data), encoding='utf-8', sep=",", dtype=str)

        crid = self.__transform_logno_to_crid()
        number_rows = self.__transform_officer_demographics_to_number_of_rows()
        beat_id = self.__transform_beat_id()
        officer_age = self.__transform_officer_demographic("age_of_involved_officers")
        officer_gender = self.__transform_officer_gender()
        officer_race = self.__transform_officer_demographic("race_of_involved_officers")
        officer_years_on_force = self.__transform_officer_demographic("years_on_force_of_officers")

        self.transformed_data.insert(0, "cr_id", crid)
        self.transformed_data.insert(1, "number_of_officer_rows", number_rows)
        self.transformed_data.insert(2, "beat_id", beat_id)
        self.transformed_data.insert(3, "officer_race", officer_race)
        self.transformed_data.insert(4, "officer_gender", officer_gender)
        self.transformed_data.insert(5, "officer_age", officer_age)
        self.transformed_data.insert(6, "officer_years_on_force", officer_years_on_force)

    def __transform_logno_to_crid(self):
        transformed_logno = self.initial_data["log_no"].transform(lambda logno: logno)

        return transformed_logno

    def __transform_officer_demographic(self, column):
        return self.initial_data[column].apply(lambda x: [] if pd.isna(x) else x.split(' | '))

    def __transform_officer_gender(self):
        def split_and_clean(input):
            if not pd.isna(input):
                return [x.strip()[0].upper() for x in input.split(" | ")]
            else:
                return []
        return self.initial_data["sex_of_involved_officers"].apply(lambda value: split_and_clean(value))

    def __transform_officer_demographics_to_number_of_rows(self):
        number_of_rows = self.initial_data["sex_of_involved_officers"].\
            transform(lambda sex: 1 if pd.isnull(sex) else len(sex.split('|')))

        return number_of_rows

    def __transform_beat_id(self):
        return self.initial_data["beat"].transform(lambda beat: self.transform_beat_id_helper(beat))

    def get_transformed_data(self):
        return self.transformed_data

    def get_non_transformable_data(self):
        return self.non_transformable_data

    def transform_beat_id_helper(self, beat):
        if type(beat) == str:
            if beat.__contains__('|'):
                beat_ids_list = beat.split('|')
                return self.validate_beat_ids(beat_ids_list)
            else:
                return int(beat) if self.beat_is_valid(int(beat)) else int()
        elif pd.isna(beat):
            return int()
        elif type(beat) == int:
            return int(beat) if self.beat_is_valid(beat) else int()
        elif type(beat) == float:
            return int(beat) if self.beat_is_valid(int(beat)) else int()

    def validate_beat_ids(self, beat_ids):
        valid_beat = int()
        for beat_id in beat_ids:
            if int(beat_id) in self.valid_beat_list:
                valid_beat = int(beat_id)
                break
        return int(valid_beat)

    def beat_is_valid(self, beat):
        if beat in self.valid_beat_list:
            return True
        else:
            return False
