import pdb

import pandas as pd

from invisible_flow.copa.data_allegation import DataAllegation
from invisible_flow.copa.data_officer_allegation import DataOfficerAllegation
from invisible_flow.copa.data_officer_unknown import DataOfficerUnknown
from invisible_flow.copa.existing_crid import ExistingCrid
from sqlalchemy.orm.exc import NoResultFound

from manage import db


class Mapper:

    def query_existing_crid_table(self):
        try:
            existing_crids = ExistingCrid.query.one().existing_crids
        except NoResultFound:
            existing_crids = ''
        return existing_crids

    def save_new_crids_to_db(self, old_crids, new_crids):
        old_crids_str = ','.join(old_crids)
        new_crids_str = ','.join(new_crids)
        concatenated_crids = f"{old_crids_str},{new_crids_str}"
        try:
            existing_crid = ExistingCrid.query.one()
            existing_crid.existing_crids = concatenated_crids
            db.session.add(existing_crid)
        except NoResultFound:
            only_new_crids = ExistingCrid(existing_crids=f"{new_crids_str}")
            db.session.add(only_new_crids)
        db.session.commit()

    def load_allegation_into_db(self, new_allegation_rows: pd.DataFrame):
        db.session.bulk_insert_mappings(DataAllegation, new_allegation_rows.to_dict(orient="records"))

    def get_existing_allegation_data(self):
        existing_data = DataAllegation.query.with_entities(DataAllegation.cr_id, DataAllegation.beat_id).all()
        return pd.DataFrame(existing_data, columns=['cr_id', 'beat_id'])

    def get_existing_officer_data(self):
        existing_data = DataOfficerAllegation.query.with_entities(DataOfficerAllegation.allegation_id,
                                                               DataOfficerAllegation.race, DataOfficerAllegation.gender,
                                                               DataOfficerAllegation.age,
                                                               DataOfficerAllegation.years_on_force).all()

        return pd.DataFrame(existing_data, columns=['allegation_id', 'race', 'gender', 'age',
                                                    'years_on_force'])

    def load_officer_into_db(self, new_officer_rows):
        db.session.bulk_insert_mappings(DataOfficerAllegation, new_officer_rows.to_dict(orient="records"))
