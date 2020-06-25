import pdb

import pandas as pd

from invisible_flow.copa.data_allegation import DataAllegation
from manage import db

class AllegationMapper:

    def load_allegation_into_db(self, new_allegation_rows: pd.DataFrame()):
        db.session.bulk_insert_mappings(DataAllegation, new_allegation_rows.to_dict(orient="records"))

    def get_existing_data(self):
        existing_data = DataAllegation.query.with_entities(DataAllegation.cr_id, DataAllegation.beat_id).all()
        return pd.DataFrame(existing_data, columns=['cr_id', 'beat_id'])
