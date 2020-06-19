from invisible_flow.constants import COPA_DB_BIND_KEY
from invisible_flow.copa.existing_crid import ExistingCrid
from invisible_flow.copa.sorter import Sorter
from manage import db
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
        expected_existing_crids = "1008899,1008889,1008888"
        expected_new_crids = "1007777,1007778"
        scraped_crids = ["1008899", "1008889", "1008888", "1007777", "1007778"]
        return expected_existing_crids, expected_new_crids, scraped_crids

    def test_query_should_return_empty_string_when_no_existing_crids(self):
        db.session.close()
        db.drop_all()
        db.create_all(bind=COPA_DB_BIND_KEY)

        test_sorter = Sorter()

        existing_crids = test_sorter.query_existing_crid_table()
        assert(existing_crids == '')

    def test_query_existing_crids_should_return_existing_crids(self, generate_variables):
        expected_existing_crids = generate_variables[0]

        test_sorter = Sorter()

        existing_crids = test_sorter.query_existing_crid_table()
        assert(existing_crids == expected_existing_crids)

    def test_parse_existing_crids_should_parse_crids(self, generate_variables):
        expected_existing_crids, expected_new_crids, scraped_crids = generate_variables
        test_sorter = Sorter()

        # parse_existing_crids has not been written yet
        test_sorter.parse_existing_crids(scraped_crids)

        assert(test_sorter.old_crids == expected_existing_crids.split(','))
        assert(test_sorter.new_crids == expected_new_crids.split(','))
