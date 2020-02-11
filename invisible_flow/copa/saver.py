from typing import List

from invisible_flow.globals_factory import GlobalsFactory
import pandas as pd

from invisible_flow.storage.storage_factory import StorageFactory


class Saver:
    def __init__(self):
        self.current_time = GlobalsFactory.get_current_datetime_utc().isoformat(sep='_').replace(':', '-')
        self.storage = StorageFactory.get_storage()

    def save_to_csv(self, list_of_series: List[pd.DataFrame], filename: str):
        if not list_of_series:
            data_bytes = b""
        else:
            data_bytes = pd.concat(list_of_series, ignore_index=True).to_csv(header=['cr_id'], index=False)\
                .encode('utf-8')

        self.storage.store_byte_string(filename, data_bytes, f"COPA_SCRAPE-{self.current_time}")
