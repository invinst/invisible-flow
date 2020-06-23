import pdb

from invisible_flow.constants import COPA_DB_BIND_KEY
from invisible_flow.copa.existing_crid import ExistingCrid
from invisible_flow.copa.sorter import Sorter
from manage import db
import pandas as pd
from pandas.testing import assert_frame_equal
import pytest


class TestSorter:

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

        test_sorter = Sorter()

        existing_crids = test_sorter.query_existing_crid_table()
        assert (existing_crids == '')

    def test_query_existing_crids_should_return_existing_crids(self, generate_variables):
        expected_existing_crids = generate_variables[0]

        test_sorter = Sorter()

        existing_crids = test_sorter.query_existing_crid_table()
        assert (existing_crids == expected_existing_crids)

    def test_parse_existing_crids_should_parse_crids(self, generate_variables):
        expected_existing_crids, expected_new_crids, scraped_crids = generate_variables
        test_sorter = Sorter()

        test_sorter.split_crids_into_new_and_old(scraped_crids)

        assert (test_sorter.old_crids == set(expected_existing_crids.split(',')))
        assert (test_sorter.new_crids == set(expected_new_crids.split(',')))

    def test_saves_new_crids_db(self, generate_variables):
        expected_existing_crids, expected_new_crids, scraped_crids = generate_variables
        test_sorter = Sorter()

        test_sorter.split_crids_into_new_and_old(scraped_crids)
        test_sorter.save_new_crids_to_db()

        actual_saved_crids = ExistingCrid.query.one().existing_crids.split(',')

        expected_saved_crids = set(scraped_crids)

        assert (set(actual_saved_crids) == expected_saved_crids)

    def test_no_change_to_existing_crids_when_there_are_no_new_crids(self):
        test_sorter = Sorter()
        grouped_crids = test_sorter.get_grouped_crids(["33333333", "1111111", "999999"])
        assert(grouped_crids.new_crids == set())
        assert(grouped_crids.existing_crids == {"33333333", "1111111", "999999"})

    def test_get_new_rows_should_return_rows_with_new_crids(self):
        test_sorter = Sorter()
        test_sorter.new_crids = ["33333333", "1111111", "999999"]
        fake_scraped_data = pd.DataFrame({
            "log_no":["33333333", "1111111", "999999","100000","100007"],
            "beat":["444","555","777","888","999"]
        })
        expected_new_rows = pd.DataFrame({
            "log_no": ["33333333", "1111111", "999999"],
            "beat": ["444", "555", "777"]
        })
        new_rows = test_sorter.get_new_allegation_rows(fake_scraped_data)
        assert_frame_equal(new_rows,expected_new_rows)