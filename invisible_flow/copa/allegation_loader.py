import pdb

import pandas as pd

from invisible_flow.copa.data_allegation import DataAllegation
from manage import db

class AllegationLoader:

    def load_allegation_into_db(self, new_allegation_rows: pd.DataFrame()):
        db.session.bulk_insert_mappings(DataAllegation, new_allegation_rows.to_dict(orient="records"))
