import pdb

import pandas as pd

from invisible_flow.constants import VALID_BEATS_AS_STR


class AllegationTransformer(object):

    def transform(self, new_rows: pd.DataFrame):
        return self.transform_beat_id(new_rows)


    def transform_beat_id(self, new_rows: pd.DataFrame):
        new_rows["beat"] = new_rows["beat"].astype(str)
        new_rows["beat"] = new_rows["beat"].apply(lambda beat: beat.split(" | "))
        new_rows["beat"] = new_rows["beat"].apply(lambda beat: self.validate_beat_ids(beat))
        return new_rows

    def validate_beat_ids(self, beat_ids):
        valid_beat = ""
        for beat_id in beat_ids:
            if beat_id in VALID_BEATS_AS_STR:
                valid_beat = beat_id
                break
        return valid_beat