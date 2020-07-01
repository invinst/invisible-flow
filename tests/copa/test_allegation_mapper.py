import pytest

from invisible_flow.constants import COPA_DB_BIND_KEY
from invisible_flow.copa.allegation_mapper import AllegationMapper
import pandas as pd
from pandas.testing import assert_frame_equal

from invisible_flow.copa.data_allegation import DataAllegation
from invisible_flow.copa.existing_crid import ExistingCrid
from manage import db


class TestAllegationMapper:

    @pytest.fixture(autouse=True)
    def set_up(self, generate_variables):
        db.session.close()
        db.drop_all()
        db.create_all(bind=COPA_DB_BIND_KEY)

        crids_in_db = ExistingCrid(existing_crids=generate_variables[0])
        db.session.add(crids_in_db)
        db.session.commit()

    @pytest.fixture
    def generate_variables(self):
        expected_existing_crids = "33333333,1111111,999999"
        expected_new_crids = "4444444,666666"
        scraped_crids = ["33333333", "1111111", "999999", "4444444", "666666"]
        return expected_existing_crids, expected_new_crids, scraped_crids

    def test_query_should_return_empty_string_when_no_existing_crids(self):
        db.session.close()
        db.drop_all()
        db.create_all(bind=COPA_DB_BIND_KEY)

        test_mapper = AllegationMapper()

        existing_crids = test_mapper.query_existing_crid_table()

        assert (existing_crids == '')

    def test_query_existing_crids_should_return_existing_crids(self, generate_variables):
        expected_existing_crids = generate_variables[0]

        test_mapper = AllegationMapper()

        existing_crids = test_mapper.query_existing_crid_table()
        assert (existing_crids == expected_existing_crids)

    def test_saves_new_crids_db(self, generate_variables):
        expected_existing_crids, expected_new_crids, scraped_crids = generate_variables

        test_mapper = AllegationMapper()

        test_mapper.save_new_crids_to_db(expected_existing_crids.split(','), expected_new_crids.split(','))

        actual_saved_crids = ExistingCrid.query.one().existing_crids.split(',')

        expected_saved_crids = set(scraped_crids)

        assert (set(actual_saved_crids) == expected_saved_crids)

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
            "cr_id": ["33333333", "1111111", "999999", "888888"],
            "beat_id": ["111", "112", "114", "115"]
        })

        test_mapper.load_allegation_into_db(fake_existing_data)

        existing_data = test_mapper.get_existing_data()
        assert_frame_equal(existing_data, fake_existing_data)
