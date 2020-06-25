import pytest

from invisible_flow.constants import COPA_DB_BIND_KEY
from invisible_flow.copa.allegation_mapper import AllegationMapper
import pandas as pd
from pandas.testing import assert_frame_equal

from invisible_flow.copa.data_allegation import DataAllegation
from manage import db

class TestAllegationMapper:

    @pytest.fixture(autouse=True)
    def set_up(self):
        db.session.close()
        db.drop_all()
        db.create_all(bind=COPA_DB_BIND_KEY)

    def test_allegation_mapper_should_load_new_rows(self):
        test_mapper = AllegationMapper()

        fake_new_rows = pd.DataFrame({
            "cr_id": ["33333333", "1111111", "999999", "100000", "100007"],
            "beat_id": ["111", "112", "114", "121", ""]
        })

        test_mapper.load_allegation_into_db(fake_new_rows)

        queried_allegation_data = DataAllegation.query.all()

        assert(len(queried_allegation_data) == len(fake_new_rows.index))

    def test_mapper_get_existing_data_should_return_existing_data(self):
        test_mapper = AllegationMapper()

        fake_existing_data = pd.DataFrame({
            "cr_id": ["33333333", "1111111", "999999","888888"],
            "beat_id": ["111", "112", "114", "115"]
        })

        test_mapper.load_allegation_into_db(fake_existing_data)

        existing_data = test_mapper.get_existing_data()
        assert_frame_equal(existing_data,fake_existing_data)
