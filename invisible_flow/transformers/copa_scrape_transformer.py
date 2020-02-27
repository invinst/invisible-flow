import re
from io import BytesIO

import pandas as pd

from invisible_flow.copa.data_area import DataArea


class CopaScrapeTransformer:

    def __init__(self):
        self.initial_data = pd.DataFrame()
        self.transformed_data = pd.DataFrame()
        self.non_transformable_data = pd.DataFrame()

    def transform(self, scraped_data: bytes):
        self.initial_data = pd.read_csv(BytesIO(scraped_data), encoding='utf-8', sep=",", dtype=str).fillna('')

        crid = self.transform_logno_to_crid()
        self.transformed_data.insert(0, "cr_id", crid)
        beat_id = self.transform_beat_to_beat_name()
        self.transformed_data.insert(1, "beat_id", beat_id)

    def transform_logno_to_crid(self):
        transformed_logno = self.initial_data["log_no"].transform(lambda logno: logno)
        return transformed_logno

    def transform_beat_to_beat_name(self):
        beat_name_table = {"": None}
        for result_pair in DataArea.query.with_entities(DataArea.name, DataArea.id):
            beat_name_table[result_pair.name] = result_pair.id

        def zero_pad(beat):
            if len(beat) == 4:
                return beat
            elif len(beat) == 3:
                return "0" + beat
            elif len(beat) > 4 and "|" in beat:
                return zero_pad(re.split(r'\D+', beat)[0])
            else:
                return ""

        transformed_beat = self.initial_data["beat"]\
            .transform(lambda beat: beat_name_table.get(zero_pad(beat))).astype('Int32')
        return transformed_beat

    def get_transformed_data(self):
        return self.transformed_data

    def get_non_transformable_data(self):
        return self.non_transformable_data
