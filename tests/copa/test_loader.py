import pytest

from manage import db
from invisible_flow.constants import COPA_DB_BIND_KEY
from tests.helpers.testing_data import transformed_data
from invisible_flow.copa.loader import Loader
from invisible_flow.copa.data_allegation import DataAllegation
from invisible_flow.copa.data_allegation import insert_allegation_into_database
import timeit


class TestLoader:

    @pytest.fixture(autouse=True)
    def set_up(self):
        db.session.close()
        db.drop_all()
        db.create_all(bind=COPA_DB_BIND_KEY)

    def test_load_data_into_empty_database(self):

        Loader().load_into_db(transformed_data)
        queried_data = DataAllegation.query.all()

        assert(len(queried_data) == len(transformed_data))
        assert(queried_data[0].cr_id == transformed_data.cr_id[0])
        assert(queried_data[4].cr_id == transformed_data.cr_id[4])

    def test_load_data_with_matches_into_database(self):
        insert_allegation_into_database(DataAllegation(cr_id="1087378"))
        insert_allegation_into_database(DataAllegation(cr_id="1087387"))

        expected_matches = [transformed_data.iloc[1], transformed_data.iloc[2]]
        expected_new_data = [transformed_data.iloc[0], transformed_data.iloc[3], transformed_data.iloc[4]]

        testLoader = Loader()
        testLoader.load_into_db(transformed_data)

        matches = testLoader.get_matches()
        assert(expected_matches[0].equals(matches[0]))
        assert(expected_matches[1].equals(matches[1]))

        new_data = testLoader.get_new_data()
        assert(expected_new_data[0].equals(new_data[0]))
        assert(expected_new_data[1].equals(new_data[1]))
        assert(expected_new_data[2].equals(new_data[2]))

    def setup_db_with_mock_data_rows(self):
        for crid in range(10000):
            new_allegation = DataAllegation(cr_id=crid)
            db.session.add(new_allegation)
        db.session.commit()
        db.session.close()

    def test_benchmark_new_loading_strategy(self):
        self.setup_db_with_mock_data_rows()

        mysetup = '''
from invisible_flow.copa.data_allegation import DataAllegation
from invisible_flow.copa.data_allegation import insert_allegation_into_database
from invisible_flow.copa.loader import Loader
from tests.helpers.testing_data import transformed_data
insert_allegation_into_database(DataAllegation(cr_id="1087378"))
insert_allegation_into_database(DataAllegation(cr_id="1087387"))
        '''

        mycode = '''
testLoader = Loader()
testLoader.load_into_db(transformed_data)
        '''
        print("----------------Benchmark for new loading strategy:")
        print(timeit.timeit(setup=mysetup, stmt=mycode, number=1000))

        db.session.query(DataAllegation).delete()
        # Clean up mock data rows

        assert(False)
