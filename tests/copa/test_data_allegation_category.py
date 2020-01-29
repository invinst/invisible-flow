import pytest

from invisible_flow.constants import COPA_DB_BIND_KEY
from invisible_flow.copa.data_allegation_category import AllegationCategory
from manage import db


class TestAllegationCategory:

    @pytest.fixture
    def get_db(self):
        db.create_all(bind=COPA_DB_BIND_KEY)

        yield db

    def get_allegation_category(self):
        return AllegationCategory(
            cr_id='cr_id',
            category='category',
            category_code='category_code',
            allegation_name='allegation_name',
            on_duty='on_duty'
        )

    def test_create_allegation_category(self):
        try:
            self.get_allegation_category()
        except Exception:
            pytest.fail('this should not have thrown an exception')

    def test_adding_allegation_category_to_db_works(self, get_db):
        cr = self.get_allegation_category()
        get_db.session.add(cr)
        get_db.session.commit()
        assert len(AllegationCategory.query.all()) == 1
        db.session.close()
