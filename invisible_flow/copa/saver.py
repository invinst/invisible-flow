from typing import List
import os

from invisible_flow.globals_factory import GlobalsFactory
import pandas as pd

from invisible_flow.storage.storage_factory import StorageFactory


class Saver:
    def __init__(self):
        self.current_time = GlobalsFactory.get_current_datetime_utc().isoformat(sep='_').replace(':', '-')
        self.storage = StorageFactory.get_storage()

    def save_to_csv(self, data_from_copa_scrape: pd.DataFrame, filename: str):
        outdir = f"local_upload/COPA_SCRAPE-{self.current_time}"
        if not os.path.exists(outdir):
            os.mkdir(outdir)
        path_to_csv_storage = outdir + "/" + filename
        data_from_copa_scrape.to_csv(path_to_csv_storage, index=False)

