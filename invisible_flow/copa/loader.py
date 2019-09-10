import numpy
import pandas as pd

from invisible_flow.copa.data_allegation import Allegation
from invisible_flow.globals_factory import GlobalsFactory
from invisible_flow.storage.storage_factory import StorageFactory
from manage import db


class Loader:

    def __init__(self):
        self.db_values = pd.DataFrame(
            Allegation.query.with_entities(Allegation.cr_id)
        ).values.flatten()
        self.partial_matches = []
        self.storage = StorageFactory.get_storage()
        self.current_date = GlobalsFactory.get_current_datetime_utc().isoformat(sep='_').replace(':', '-')

    def load_copa_db(self, augmented_data: pd.DataFrame):
        copa_column_names = ["cr_id", "beat_id", "incident_date"]
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
                if cr.beat_id != db_row_match_log_no.beat_id or cr.incident_date != db_row_match_log_no.incident_date:
                    self.partial_matches.append(cr)

        allegation_rows = Allegation.query.all()
        df = pd.DataFrame(
            [(row.cr_id, row.beat_id, row.incident_date) for row in allegation_rows],
            columns=copa_column_names
        )

        if len(df) > 0:
            self.storage.store_string(
                'changed_allegation.csv',
                df.to_csv(index=False),
                f'Scrape-{self.current_date}/errors'
            )
            return {
                'partial_matches': self.partial_matches
            }

        return {}

    # TODO handle partial matches where db row is missing data that is populated in augmented row
    #  this should update the db row and also put out a file under errors/updated_allegations.csv
