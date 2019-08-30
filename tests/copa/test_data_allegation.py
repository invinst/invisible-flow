import pytest

from invisible_flow.constants import COPA_DB_BIND_KEY
from invisible_flow.copa.data_allegation import Allegation
from manage import db


class TestAllegation:

    @pytest.fixture
    def get_db(self):
        db.create_all(bind=COPA_DB_BIND_KEY)

        yield db

    def get_allegation(self):
        return Allegation(
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

    def test_create_allegation(self):
        try:
            self.get_allegation()
        except Exception:
            pytest.fail('this should not have thrown an exception')

    def test_adding_copa_record_to_db_works(self, get_db):
        cr = self.get_allegation()
        get_db.session.add(cr)
        get_db.session.commit()
        assert len(Allegation.query.all()) == 1
