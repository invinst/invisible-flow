import pandas as pd

from manage import db
from invisible_flow.copa.data_allegation import DataAllegation


class Loader:

    def __init__(self):
        self.existing_crid = pd.DataFrame(
            DataAllegation.query.with_entities(DataAllegation.cr_id)
        ).values.flatten().tolist()

    def load_into_db(self, transformed_data: pd.DataFrame):

        for row in transformed_data.itertuples():

            if row.cr_id not in self.existing_crid:
                new_allegation = DataAllegation(cr_id=row.cr_id)
                db.session.add(new_allegation)

        db.session.commit()
        db.session.close()

# import pandas as pd
#
# from invisible_flow.copa.data_allegation import DataAllegation
# from invisible_flow.globals_factory import GlobalsFactory
# from invisible_flow.storage.storage_factory import StorageFactory
# from manage import db
# from datetime import datetime
#
#
# class Loader:
#
#     def __init__(self):
#         self.log_nos = pd.DataFrame(
#             DataAllegation.query.with_entities(DataAllegation.cr_id)
#         ).values.flatten().tolist()
#         self.partial_matches = []
#         self.db_rows_added = []
#         self.error_notes = pd.DataFrame()
#         self.changed_allegations = pd.DataFrame()
#         self.storage = StorageFactory.get_storage()
#         self.current_date = GlobalsFactory.get_current_datetime_utc().isoformat(sep='_').replace(':', '-')
#
#     def get_error_note(self, column_name: str, cr_id: str, db_value: str, allegation_value: str) -> str:
#         return f'{cr_id}, column {column_name} contained the value ' \
#                f'{db_value} ' \
#                f'in the database but ' \
#                f'the new dataset contains the value {allegation_value} '
#
#     def load_copa_db(self, augmented_data: pd.DataFrame):
#         copa_column_names = ["cr_id", "beat_id", "incident_date"]
#         for row in augmented_data.iterrows():
#             log_no = row[1]["log_no"]
#             datetime_string = str(row[1]["complaint_date"]).replace('T', ' ')
#             datetime_object = datetime.strptime(datetime_string, '%Y-%m-%d %H: %M: %S.%f')
#
#             current_allegation = DataAllegation(
#                 cr_id=str(log_no),
#                 beat_id=str(row[1]["beat"]),
#                 incident_date=datetime_object
#             )
#
#             if log_no not in self.log_nos:
#                 db.session.add(current_allegation)
#                 db.session.commit()
#                 self.log_nos.append(log_no)
#                 self.db_rows_added.append(current_allegation)
#             else:
#                 db_row_match_log_no = DataAllegation.query.filter_by(cr_id=str(log_no)).all()[0]
#                 had_partial_match = False
#                 for column_name in DataAllegation.__table__.columns.keys():
#                     if current_allegation[column_name] != db_row_match_log_no[column_name]:
#                         had_partial_match = True
#                         self.error_notes = self.error_notes.append(
#                             {
#                                 "error_notes":
#                                     self.get_error_note(
#                                          column_name,
#                                          current_allegation.cr_id,
#                                          db_row_match_log_no[column_name],
#                                          current_allegation[column_name]
#                                     )
#                             },
#                             ignore_index=True
#                         )
#
#                 if had_partial_match:
#                     self.partial_matches.append(current_allegation)
#
#         self.changed_allegations = pd.DataFrame(
#             [(row.cr_id, row.beat_id, row.incident_date) for row in self.partial_matches],
#             columns=copa_column_names
#         )
#
#         if len(self.changed_allegations) > 0:
#             self.storage.store_byte_string(
#                 'changed_allegation.csv',
#                 self.changed_allegations.to_csv(index=False).encode('utf-8'),
#                 f'Scrape-{self.current_date}/load_errors'
#             )
#             self.storage.store_byte_string(
#                 'error_notes.csv',
#                 self.error_notes.to_csv(index=False).encode('utf-8'),
#                 f'Scrape-{self.current_date}/load_errors'
#             )
#
#     # TODO handle partial matches where db row is missing data that is populated in augmented row
#     #  this should update the db row and also put out a file under errors/updated_allegations.csv
