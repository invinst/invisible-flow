import pdb

from invisible_flow.globals_factory import GlobalsFactory
import pandas as pd

from invisible_flow.storage.storage_factory import StorageFactory


class OfficerSaver:
    def __init__(self):
        self.current_time = GlobalsFactory.get_current_datetime_utc().isoformat(sep='_').replace(':', '-')
        self.storage = StorageFactory.get_storage()
        self.officer_allegation_df = pd.DataFrame()
        self.officer_unknown_demographics_df = pd.DataFrame()

    def save_officer_to_csv(self, old_officer_data: pd.DataFrame, new_officer_data: pd.DataFrame):
        old_officer_demographics, old_officer_allegation = self.split_officer_data(old_officer_data)
        self.save(old_officer_allegation, 'old_officer_allegation_data.csv')
        self.save(old_officer_demographics, 'old_officer_demographic_data.csv')

        new_officer_demographics, new_officer_allegation = self.split_officer_data(new_officer_data)
        self.save(new_officer_allegation, 'new_officer_allegation_data.csv')
        self.save(new_officer_demographics, 'new_officer_demographic_data.csv')

    def split_officer_data(self,data_from_copa_scrape: pd.DataFrame):
        officer_demographic_data = data_from_copa_scrape.filter(['age', 'gender', 'race', 'years_on_force'], axis='columns')
        officer_allegation_data = data_from_copa_scrape.drop(['age', 'gender', 'race', 'years_on_force'], axis='columns')
        return officer_demographic_data, officer_allegation_data

    def save(self, data, filename):
        data_bytes = data.to_csv(index=False).encode('utf-8')
        self.storage.store_byte_string(filename, data_bytes, f"COPA_SCRAPE-{self.current_time}")
