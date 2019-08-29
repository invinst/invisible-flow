import pytest

from invisible_flow.constants import VALID_STATUSES, COPA_DB_BIND_KEY
from invisible_flow.copa.data_allegation import CopaRecord
from manage import db


class TestCopaRecord:

    @pytest.fixture
    def get_db(self):
        db.create_all(bind=COPA_DB_BIND_KEY)

        yield db

    @pytest.mark.parametrize('status', VALID_STATUSES)
    def test_copa_record_entity_allows_valid_statuses(self, status):
        try:
            CopaRecord(status=status)
        except Exception:
            pytest.fail('this should not have thrown an exception')

    def test_adding_copa_record_to_db_works(self, get_db):
        for status in VALID_STATUSES:
            get_db.session.add(CopaRecord(status=status))
        get_db.session.commit()
        assert len(CopaRecord.query.all()) == len(VALID_STATUSES)
