import pandas as pd

from invisible_flow.copa.data_allegation import Allegation
from manage import db


class Loader:

    def load_copa_db(self, augmented_data: pd.DataFrame):
        cr_ids = pd.DataFrame(
            Allegation.query.with_entities(Allegation.cr_id)
        )
        print(cr_ids)
        for row in augmented_data.iterrows():
            cr = Allegation(
                cr_id=row[1]["log_no"],
                beat_id=row[1]["beat"],
                incident_date=row[1]["complaint_date"]
            )
# TODO verify that the log number in this row exists in the cr_ids collection AND if it does, pair data, if NOT
# just add it
            db.session.add(cr)
            db.session.commit()


# if all row data matches, disregard row
# if not all row data matches, update row???
