from invisible_flow.globals_factory import GlobalsFactory
import pandas as pd

from invisible_flow.storage.storage_factory import StorageFactory


class Saver:
    def __init__(self):
        self.current_time = GlobalsFactory.get_current_datetime_utc().isoformat(sep='_').replace(':', '-')
        self.storage = StorageFactory.get_storage()

    def save_to_csv(self, data_from_copa_scrape: pd.DataFrame, filename: str):
        data_bytes = data_from_copa_scrape.to_csv(index=False).encode('utf-8')
        self.storage.store_byte_string(filename, data_bytes, f"COPA_SCRAPE-{self.current_time}")


def strip_zeroes_from_beat_id(df_with_beat_id_col: pd.DataFrame):
    if not df_with_beat_id_col.empty:
        df_with_beat_id_col["beat_id"] = df_with_beat_id_col["beat_id"]. \
            transform(lambda beat: '' if beat == 0 else beat)

    return df_with_beat_id_col


def cast_col_to_int(dataframe: pd.DataFrame, column_label: str):
    copy = dataframe.copy()

    copy[column_label] = dataframe[column_label].astype("int64")
    return copy
