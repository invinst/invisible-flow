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
            summary='summary',
            allegation_status='status',
            police_shooting='no',
            case_type='case_type',
            investigating_agency='investigating_agency'
        )

    def get_allegation_with_null_values_for_added_columns(self):
        return Allegation(
            cr_id='dr_id',
            add1='add1',
            add2='add2',
            beat_id='beat_id',
            city='city',
            incident_date='incident_date',
            is_officer_complaint=True,
            location='location',
            summary='summary')

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

    def test_new_fields_are_added(self, get_db):
        record = Allegation.query.first()
        allegation_status = record.allegation_status
        police_shooting = record.police_shooting
        case_type = record.case_type
        investigating_agency = record.investigating_agency

        assert allegation_status == 'status'
        assert police_shooting == 'no'
        assert case_type == 'case_type'
        assert investigating_agency == 'investigating_agency'

    def test_new_fields_default_to_null(self, get_db):
        record = self.get_allegation_with_null_values_for_added_columns()
        get_db.session.add(record)
        get_db.session.commit()

        allegation_fetched_from_db = Allegation.query.get('dr_id')
        allegation_status = allegation_fetched_from_db.allegation_status
        police_shooting = allegation_fetched_from_db.police_shooting
        case_type = allegation_fetched_from_db.case_type
        investigating_agency = allegation_fetched_from_db.investigating_agency

        assert allegation_status is None
        assert police_shooting is None
        assert case_type is None
        assert investigating_agency is None
