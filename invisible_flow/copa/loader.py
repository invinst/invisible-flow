import pandas as pd
# These libraries lack mypy typing
import numpy as np  # type: ignore
from psycopg2.extensions import register_adapter, AsIs  # type: ignore

from manage import db
from invisible_flow.copa.data_allegation import DataAllegation

register_adapter(np.int32, AsIs)


class Loader:

    def __init__(self):
        self.existing_crid = pd.DataFrame(
            DataAllegation.query.with_entities(DataAllegation.cr_id)
        ).values.flatten().tolist()
        self.matches = []
        self.new_data = []

    def load_into_db(self, transformed_data: pd.DataFrame):

        for row in transformed_data.itertuples():

            if row.cr_id not in self.existing_crid:
                new_allegation = DataAllegation(cr_id=row.cr_id,
                                                beat_id=(None if np.isnan(row.beat_id) else row.beat_id))
                db.session.add(new_allegation)
                self.new_data.append(transformed_data.iloc[row[0]])
            else:
                self.matches.append(transformed_data.iloc[row[0]])

        db.session.commit()
        db.session.close()

    def get_matches(self):
        return self.matches

    def get_new_data(self):
        return self.new_data
