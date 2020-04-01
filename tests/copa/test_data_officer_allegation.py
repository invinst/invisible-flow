import pytest
import datetime
from invisible_flow.constants import COPA_DB_BIND_KEY
from invisible_flow.copa.data_officer_allegation import DataOfficerAllegation
from manage import db


class TestDataOfficerAllegation:

    @pytest.fixture(autouse=True)
    def get_db(self):
        db.session.close()
        # db.drop_all()
        DataOfficerAllegation.query.filter_by(id=1).delete()
        db.session.commit()
        db.create_all(bind=COPA_DB_BIND_KEY)

        yield db

    def get_data_officer_allegation(self):
        return DataOfficerAllegation(
            id=1,
            allegation_id='C227980',
            allegation_category_id=2,
            officer_id=3,
            start_date=datetime.datetime(2001, 4, 27),
            end_date=datetime.datetime(2003, 1, 17),
            officer_age=47,
            recc_finding='Y',
            recc_outcome='recc_outcome',
            final_finding='Y',
            final_outcome='final_outcome',
            final_outcome_class='final_outcome_class',
            disciplined=True,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow()
        )

    def test_create_data_officer_allegation(self):
        try:
            self.get_data_officer_allegation()
        except Exception:
            pytest.fail('this should not have thrown an exception')

    def test_adding_data_officer_allegation_to_db_works(self, get_db):
        cr = self.get_data_officer_allegation()
        db.session.add(cr)
        db.session.commit()

        try:
            DataOfficerAllegation.query.filter_by(id=1)
        except Exception:
            pytest.fail('Was not added correctly')

        DataOfficerAllegation.query.filter_by(id=1).delete()
        db.session.commit()
        db.session.close()
