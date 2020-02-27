import datetime

import pytest

from invisible_flow.copa.data_allegation import DataAllegation
from manage import db


class TestDataAllegation:

    @pytest.fixture(autouse=True)
    def get_db(self):
        db.session.query(DataAllegation).delete()
        db.session.commit()
        yield db
        db.session.close()

    def get_data_allegation(self):
        return DataAllegation(
            cr_id='cr_id',
            summary='summary',
            add1='add1',
            add2='add2',
            city='city',
            incident_date=datetime.datetime.utcnow(),
            is_officer_complaint=True,
            location='location',
            old_complaint_address='old_complaint_address',
            subjects={"Bassil Abdelal", "Richie Cole", "Omar Young", "Leevon Carter"},
            point='0101000020E61000009FB3603DC9EA55C0138E6A227DD84440',
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow()
        )

    def test_create_data_allegation(self):
        try:
            self.get_data_allegation()
        except Exception:
            pytest.fail('this should not have thrown an exception')

    def test_adding_copa_record_to_db_works(self, get_db):
        cr = self.get_data_allegation()
        get_db.session.add(cr)
        get_db.session.commit()
        assert len(DataAllegation.query.all()) == 1
        get_db.session.close()
