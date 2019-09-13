import pandas as pd

from invisible_flow.copa.data_allegation import Allegation
from invisible_flow.globals_factory import GlobalsFactory
from invisible_flow.storage.storage_factory import StorageFactory
from manage import db


class Loader:

    def __init__(self):
        self.db_values = pd.DataFrame(
            Allegation.query.with_entities(Allegation.cr_id)
        ).values.flatten().tolist()
        self.partial_matches = []
        self.error_notes = pd.DataFrame()
        self.storage = StorageFactory.get_storage()
        self.current_date = GlobalsFactory.get_current_datetime_utc().isoformat(sep='_').replace(':', '-')

    def get_error_note(self, column_name: str, cr_id: str, db_value: str, allegation_value: str) -> str:
        return f'{cr_id}, column {column_name} contained the value ' \
               f'{db_value} ' \
               f'in the database but ' \
               f'the new dataset contains the value {allegation_value} '

    def load_copa_db(self, augmented_data: pd.DataFrame):
        copa_column_names = ["cr_id", "beat_id", "incident_date"]
        for row in augmented_data.iterrows():
            cr = Allegation(
                cr_id=str(row[1]["log_no"]),
                beat_id=str(row[1]["beat"]),
                incident_date=str(row[1]["complaint_date"])
            )
            if row[1]["log_no"] not in self.db_values:
                db.session.add(cr)
                db.session.commit()
                self.db_values.append(row[1]["log_no"])
            else:
                db_row_match_log_no = Allegation.query.filter_by(cr_id=row[1]["log_no"]).all()[0]
                had_partial_match = False
                for column_name in Allegation.__table__.columns.keys():
                    if cr[column_name] != db_row_match_log_no[column_name]:
                        had_partial_match = True
                        self.error_notes = self.error_notes.append(
                            {
                                "error_notes":
                                    self.get_error_note(
                                         column_name,
                                         cr.cr_id,
                                         db_row_match_log_no[column_name],
                                         cr[column_name]
                                    )
                            },
                            ignore_index=True
                        )

                if had_partial_match:
                    self.partial_matches.append(cr)

        df = pd.DataFrame(
            [(row.cr_id, row.beat_id, row.incident_date) for row in self.partial_matches],
            columns=copa_column_names
        )

        if len(df) > 0:
            self.storage.store_string(
                'changed_allegation.csv',
                df.to_csv(index=False),
                f'Scrape-{self.current_date}/load_errors'
            )
            self.storage.store_string(
                'error_notes.csv',
                self.error_notes.to_csv(index=False),
                f'Scrape-{self.current_date}/load_errors'
            )
            return {
                'partial_matches': self.partial_matches
            }

        return {}

    # TODO handle partial matches where db row is missing data that is populated in augmented row
    #  this should update the db row and also put out a file under errors/updated_allegations.csv
