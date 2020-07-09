from invisible_flow.globals_factory import GlobalsFactory
import pandas as pd

from invisible_flow.storage.storage_factory import StorageFactory


class OfficerSaver:
    def __init__(self):
        self.current_time = GlobalsFactory.get_current_datetime_utc().isoformat(sep='_').replace(':', '-')
        self.storage = StorageFactory.get_storage()
        self.officer_allegation_df = pd.DataFrame()
        self.officer_unknown_demographics_df = pd.DataFrame()

    def save_officer_to_csv(self, data_from_copa_scrape: pd.DataFrame, filename: str):
        # split data into officer_allegation and officer_unknown_demographics
        # save officer_allegation df to csv
        # save officer_unknown_demographics df to csv

        data_bytes = data_from_copa_scrape.to_csv(index=False).encode('utf-8')
        self.storage.store_byte_string(filename, data_bytes, f"COPA_SCRAPE-{self.current_time}")

    def split_officer_allegation(self,data_from_copa_scrape: pd.DataFrame):
        pass