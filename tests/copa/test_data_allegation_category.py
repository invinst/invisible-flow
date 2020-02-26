import datetime

import pytest

from invisible_flow.constants import COPA_DB_BIND_KEY
from invisible_flow.copa.data_allegation_category import DataAllegationCategory
from manage import db


class TestDataAllegationCategory:

    @pytest.fixture(autouse=True)
    def get_db(self):
        db.session.close()
        DataAllegationCategory.__table__.drop(db.get_engine(bind=COPA_DB_BIND_KEY))
        DataAllegationCategory.__table__.create(db.get_engine(bind=COPA_DB_BIND_KEY))
        yield db
        DataAllegationCategory.__table__.drop(db.get_engine(bind=COPA_DB_BIND_KEY))
        DataAllegationCategory.__table__.create(db.get_engine(bind=COPA_DB_BIND_KEY))
        db.session.close()

    def get_data_allegation_category(self):
        return DataAllegationCategory(
            id=1,
            category='category',
            category_code='category_code',
            allegation_name='allegation_name',
            on_duty=True,
            citizen_dept='citizen_dept',
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow()

        )

    def test_create_data_allegation_category(self):
        try:
            self.get_data_allegation_category()
        except Exception:
            pytest.fail('this should not have thrown an exception')

    def test_adding_data_allegation_category_to_db_works(self, get_db):
        cr = self.get_data_allegation_category()
        get_db.session.add(cr)
        get_db.session.commit()
        assert len(DataAllegationCategory.query.all()) == 1
        db.session.close()
