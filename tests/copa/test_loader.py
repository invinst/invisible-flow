import pytest

from invisible_flow.copa.data_allegation import DataAllegation
from invisible_flow.copa.data_allegation import insert_allegation_into_database
from invisible_flow.copa.data_officer_allegation import DataOfficerAllegation
from invisible_flow.copa.loader import Loader
from manage import db
from tests.helpers.testing_data import transformed_data


class TestLoader:

    @pytest.fixture(autouse=True)
    def set_up(self):
        db.session.query(DataAllegation).delete()
        db.session.query(DataOfficerAllegation).delete()
        db.session.commit()
        db.session.close()
        yield db
        db.session.query(DataAllegation).delete()
        db.session.query(DataOfficerAllegation).delete()
        db.session.commit()
        db.session.close()

    def test_load_data_into_empty_database(self):

        Loader().load_into_db(transformed_data)
        queried_data = DataAllegation.query.all()

        assert(len(queried_data) == len(transformed_data))
        assert(queried_data[0].cr_id == transformed_data.cr_id[0])
        assert(queried_data[0].beat_id == transformed_data.beat_id[0])
        assert(queried_data[4].cr_id == transformed_data.cr_id[4])

    def test_load_data_with_matches_into_database(self):
        insert_allegation_into_database(DataAllegation(cr_id="1087378"))
        insert_allegation_into_database(DataAllegation(cr_id="1087387"))

        expected_matches = [transformed_data.iloc[1], transformed_data.iloc[2]]
        expected_new_data = [transformed_data.iloc[0], transformed_data.iloc[3], transformed_data.iloc[4]]

        test_loader = Loader()
        test_loader.load_into_db(transformed_data)

        matches = test_loader.get_matches()
        assert(expected_matches[0].equals(matches[0]))
        assert(expected_matches[1].equals(matches[1]))

        new_data = test_loader.get_new_data()
        assert(len(expected_new_data) == 3)
        assert(expected_new_data[0].equals(new_data[0]))
        assert(expected_new_data[1].equals(new_data[1]))
        assert(expected_new_data[2].equals(new_data[2]))
