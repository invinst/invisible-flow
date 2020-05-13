from pandas.testing import assert_frame_equal

import pytest

from invisible_flow.copa.data_officer_allegation import DataOfficerAllegation
from manage import db
from invisible_flow.constants import COPA_DB_BIND_KEY
from tests.helpers.testing_data import transformed_data_with_rows, transformed_data_with_beat_id, \
    expected_transformed_data_with_beat_id, expected_load_data
from invisible_flow.copa.loader import Loader
from invisible_flow.copa.data_allegation import DataAllegation

from invisible_flow.copa.data_officer_unknown import DataOfficerUnknown
from invisible_flow.copa.data_allegation import insert_allegation_into_database
import pandas as pd


class TestLoader:

    @pytest.fixture(autouse=True)
    def set_up(self):
        db.session.close()
        db.drop_all()
        db.create_all(bind=COPA_DB_BIND_KEY)

    def test_load_data_into_empty_database(self):
        # fixed; swapped place of transformed_data_with_rows with transformed_data_with_beat_id
        Loader().load_into_db(transformed_data_with_beat_id)
        queried_allegation_data = DataAllegation.query.all()

        assert (len(queried_allegation_data) == len(transformed_data_with_rows))
        assert (queried_allegation_data[0].cr_id == transformed_data_with_rows.cr_id[0])
        assert (queried_allegation_data[4].cr_id == transformed_data_with_rows.cr_id[4])

        queried_officer_data = DataOfficerAllegation.query.all()
        assert (len(queried_officer_data) == transformed_data_with_beat_id['number_of_officer_rows'].sum())

        fourth_cr_id = transformed_data_with_beat_id['cr_id'][2]
        assert (queried_officer_data[3].allegation_id == fourth_cr_id)

    def test_get_new_data(self):
        expected_new_data = expected_load_data

        testLoader = Loader()
        testLoader.load_into_db(expected_transformed_data_with_beat_id)

        new_data = testLoader.get_new_data()
        assert_frame_equal(new_data, expected_new_data)

    def test_get_matches(self):
        expected_matches = expected_load_data

        testLoader = Loader()

        testLoader.load_into_db(expected_transformed_data_with_beat_id)
        testLoader.load_into_db(expected_transformed_data_with_beat_id)

        matches = testLoader.get_matches()

        assert_frame_equal(matches, expected_matches, check_dtype=False)

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

    @pytest.mark.focus
    def test_load_officer_data(self):
        testLoader = Loader()
        transformed_data_with_officers = pd.DataFrame({
            'cr_id': ["1008899"],
                        'number_of_officer_rows': [1],
                        'beat_id': [433],
                        'officers': [
                            pd.Series([{
                                 'age': 30,
                                 'race': 'caucasian',
                                 'gender': 'f',
                                 'years_on_force': 4
                            }])]

        })
        testLoader.load_into_db(transformed_data_with_officers)
        queried_data_officerunknown = DataOfficerUnknown.query.all()
        assert(len(queried_data_officerunknown) == 1)
