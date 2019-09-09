import numpy
import pandas as pd

from invisible_flow.copa.data_allegation import Allegation
from manage import db


class Loader:

    def __init__(self):
        self.db_values = pd.DataFrame(
            Allegation.query.with_entities(Allegation.cr_id)
        ).values.flatten()
        self.partial_matches = []

    def load_copa_db(self, augmented_data: pd.DataFrame):
        for row in augmented_data.iterrows():
            cr = Allegation(
                cr_id=row[1]["log_no"],
                beat_id=row[1]["beat"],
                incident_date=row[1]["complaint_date"]
            )
            if numpy.isin(self.db_values, row[1]["log_no"]).all():
                db.session.add(cr)
                db.session.commit()
                numpy.append(self.db_values, row[1]["log_no"])
            else:
                db_row_match_log_no = Allegation.query.filter_by(cr_id=row[1]["log_no"]).all()[0]
                if cr.beat_id != db_row_match_log_no.beat_id or cr.incident_date != db_row_match_log_no.beat_id:
                    self.partial_matches.append(cr)
        return {
            'partial_matches': self.partial_matches
        }

    # TODO convert array of Allegation objects to changed_allegation.csv
    #  upload changed_allegation.csv to gcp under /errors
    #  handle partial matches where db row is missing data populated in augmented row
    #  this should update the db row and also put out a file under errors/updated_allegations.csv
