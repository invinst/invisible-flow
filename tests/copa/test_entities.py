import pytest

from invisible_flow.constants import VALID_STATUSES, COPA_DB_BIND_KEY
from invisible_flow.copa.data_allegation import CopaRecord
from manage import db


class TestCopaRecord:

    @pytest.fixture
    def get_db(self):
        db.create_all(bind=COPA_DB_BIND_KEY)

        yield db

    def test_create_copa_record(self):
        try:
            CopaRecord(
               cr_id='cr_id',
               add1='add1',
               add2='add2',
               beat_id='beat_id',
               city='city',
               incident_date='incident_date',
               is_officer_complaint=True,
               location='location',
               summary='summary'
            )
        except Exception:
            pytest.fail('this should not have thrown an exception')

    def test_adding_copa_record_to_db_works(self, get_db):
        cr = CopaRecord(
            cr_id='cr_id',
            add1='add1',
            add2='add2',
            beat_id='beat_id',
            city='city',
            incident_date='incident_date',
            is_officer_complaint=True,
            location='location',
            summary='summary'
        )
        get_db.session.add(cr)
        get_db.session.commit()
        assert len(CopaRecord.query.all()) == 1

