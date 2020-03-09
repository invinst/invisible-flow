import pytest

from manage import db
from invisible_flow.constants import COPA_DB_BIND_KEY
from tests.helpers.testing_data import transformed_data_with_rows
from tests.helpers.testing_data import transformed_data
from invisible_flow.copa.loader import Loader
from invisible_flow.copa.data_allegation import DataAllegation
from invisible_flow.copa.data_allegation import insert_allegation_into_database
import pandas as pd


class TestLoader:

    @pytest.fixture(autouse=True)
    def set_up(self):
        db.session.close()
        db.drop_all()
        db.create_all(bind=COPA_DB_BIND_KEY)

    def test_load_data_into_empty_database(self):
        Loader().load_into_db(transformed_data_with_rows)
        queried_data = DataAllegation.query.all()

        assert (len(queried_data) == len(transformed_data_with_rows))
        assert (queried_data[0].cr_id == transformed_data_with_rows.cr_id[0])
        assert (queried_data[4].cr_id == transformed_data_with_rows.cr_id[4])

    def test_load_data_with_matches_into_database(self):
        insert_allegation_into_database(DataAllegation(cr_id="1087378"))
        insert_allegation_into_database(DataAllegation(cr_id="1087387"))

        expected_matches = [transformed_data_with_rows.iloc[1], transformed_data_with_rows.iloc[2]]
        expected_new_data = [pd.Series(transformed_data.iloc[0][0]),
                             pd.Series(transformed_data.iloc[3][0]),
                             pd.Series(transformed_data.iloc[4][0])]

        testLoader = Loader()
        testLoader.load_into_db(transformed_data_with_rows)

        matches = testLoader.get_matches()

        assert (pd.Series(expected_matches[0][0]).equals(matches[0]))
        assert (pd.Series(expected_matches[1][0]).equals(matches[1]))

        new_data = testLoader.get_new_data()
<<<<<<< HEAD
        assert(expected_new_data[0].equals(new_data[0]))
        assert(expected_new_data[1].equals(new_data[1]))
        assert(expected_new_data[2].equals(new_data[2]))

    def setup_db_with_mock_data_rows(self):
        for crid in range(10000):
            new_allegation = DataAllegation(cr_id=crid)
            db.session.add(new_allegation)
        db.session.commit()
        db.session.close()
=======

        assert (expected_new_data[0].equals(new_data[0]))
        assert (expected_new_data[1].equals(new_data[1]))
        assert (expected_new_data[2].equals(new_data[2]))
>>>>>>> [#81][Kyle/Jovanka] Fix tests related to data officer allegations; story values as Series; replace missing value in test fixture
