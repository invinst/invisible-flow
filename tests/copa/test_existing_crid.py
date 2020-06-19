import pytest

from invisible_flow.constants import COPA_DB_BIND_KEY
from invisible_flow.copa.existing_crid import ExistingCrid
from manage import db


class TestDataAllegation:

    @pytest.fixture(autouse=True)
    def get_db(self):
        db.session.close()
        db.drop_all()
        db.create_all(bind=COPA_DB_BIND_KEY)

        yield db

    def get_existing_crid(self):
        return ExistingCrid(
            existing_crids='existing_crids'
        )

    def test_create_existing_crid(self):
        try:
            self.get_existing_crid()
        except Exception:
            pytest.fail('this should not have thrown an exception')

    def test_storing_existing_crid_to_db_works(self, get_db):
        existing_crid = self.get_existing_crid()
        get_db.session.add(existing_crid)
        get_db.session.commit()
        assert len(ExistingCrid.query.all()) == 1
