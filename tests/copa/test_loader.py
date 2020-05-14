# flake8: noqa
import pandas as pd
import pytest
from unittest.mock import patch

from sqlalchemy.exc import IntegrityError

from invisible_flow.copa.data_officer_allegation import DataOfficerAllegation
from manage import db
from invisible_flow.constants import COPA_DB_BIND_KEY
from tests.helpers.testing_data import transformed_data_with_rows, transformed_data_with_beat_id
from tests.helpers.testing_data import transformed_data
from invisible_flow.copa.loader import Loader
from invisible_flow.copa.data_allegation import DataAllegation
from invisible_flow.copa.data_allegation import insert_allegation_into_database


class TestLoader:

    @pytest.fixture(autouse=True)
    def set_up(self):
        db.session.close()
        db.drop_all()
        db.create_all(bind=COPA_DB_BIND_KEY)

    def test_load_data_into_empty_database(self):
        Loader().load_into_db(transformed_data_with_rows)
        queried_allegation_data = DataAllegation.query.all()

        assert (len(queried_allegation_data) == len(transformed_data_with_rows))
        assert (queried_allegation_data[0].cr_id == transformed_data_with_rows.cr_id[0])
        assert (queried_allegation_data[4].cr_id == transformed_data_with_rows.cr_id[4])

        queried_officer_data = DataOfficerAllegation.query.all()
        assert (len(queried_officer_data) == transformed_data_with_rows['number_of_officer_rows'].sum())

        fourth_cr_id = transformed_data_with_rows['cr_id'][2]
        assert (queried_officer_data[3].allegation_id == fourth_cr_id)

    def test_load_data_with_matches_into_database(self):
        insert_allegation_into_database(DataAllegation(cr_id="1087378"))
        insert_allegation_into_database(DataAllegation(cr_id="1087387"))

        testLoader = Loader()
        queried_officer_data = DataOfficerAllegation.query.all()
        testLoader.load_into_db(transformed_data_with_rows)
        assert (len(queried_officer_data) == len(DataOfficerAllegation.query.all()))

    @patch('manage.db.session.commit', side_effect=IntegrityError('Hi Adeolu'))
    def test_get_matches(self):
        expected_matches = pd.DataFrame([{'crid': "1087378", 'beat_id': "555"},
                                         {'crid': "1087387", 'beat_id': "001"}])
        expected_new_data = pd.DataFrame([{'crid': "1087777", 'beat_id': "556"},
                                          {'crid': "108799", 'beat_id': "002"}])

        testLoader = Loader()
        testLoader.load_into_db(transformed_data_with_rows)

        matches = testLoader.get_matches()

        assert (transformed_data_with_rows.equals(matches))
        # assert (pd.Series(expected_matches[1][0]).equals(matches[1]))

        new_data = testLoader.get_new_data()

        assert (transformed_data.equals(new_data))
        # assert(expected_new_data[0].equals(new_data[0]))
        # assert(expected_new_data[1].equals(new_data[1]))
        # assert(expected_new_data[2].equals(new_data[2]))

    def setup_db_with_mock_data_rows(self):
        for crid in range(10000):
            new_allegation = DataAllegation(cr_id=crid)
            db.session.add(new_allegation)
        db.session.commit()
        db.session.close()

    def test_load_data_with_beat_id(self):
        testLoader = Loader()
        testLoader.load_into_db(transformed_data_with_beat_id)

        queried_data_allegation = DataAllegation.query.all()
        assert (queried_data_allegation[0].beat_id == 111)
