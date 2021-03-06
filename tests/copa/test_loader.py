import pandas as pd
from pandas.testing import assert_frame_equal

import pytest

from invisible_flow.copa.data_officer_allegation import DataOfficerAllegation
from manage import db
from invisible_flow.constants import COPA_DB_BIND_KEY
from tests.helpers.testing_data import transformed_data_with_beat_id, \
    expected_transformed_data_with_beat_id, expected_load_data
from invisible_flow.copa.loader import Loader
from invisible_flow.copa.data_allegation import DataAllegation
from invisible_flow.copa.data_officer_unknown import DataOfficerUnknown


class TestLoader:

    @pytest.fixture(autouse=True)
    def set_up(self):
        db.session.close()
        db.drop_all()
        db.create_all(bind=COPA_DB_BIND_KEY)

    def test_load_data_into_empty_database(self):
        Loader().load_into_db(expected_transformed_data_with_beat_id)
        queried_allegation_data = DataAllegation.query.all()

        assert (len(queried_allegation_data) == len(transformed_data_with_beat_id))
        assert (queried_allegation_data[0].cr_id == transformed_data_with_beat_id.cr_id[0])
        assert (queried_allegation_data[4].cr_id == transformed_data_with_beat_id.cr_id[4])

        queried_officer_data = DataOfficerAllegation.query.all()
        assert (len(queried_officer_data) == expected_transformed_data_with_beat_id['number_of_officer_rows'].sum())

        fourth_cr_id = transformed_data_with_beat_id['cr_id'][2]
        assert (queried_officer_data[3].allegation_id == fourth_cr_id)

    def test_get_new_data(self):
        expected_new_data = expected_load_data

        testLoader = Loader()
        testLoader.load_into_db(expected_transformed_data_with_beat_id)

        new_data = testLoader.get_new_allegation_data()
        assert_frame_equal(new_data, expected_new_data, check_dtype=False, check_like=True)

    def test_get_matches(self):
        expected_matches = expected_load_data

        testLoader = Loader()

        testLoader.load_into_db(expected_transformed_data_with_beat_id)
        testLoader.load_into_db(expected_transformed_data_with_beat_id)

        matches = testLoader.get_allegation_matches()
        assert_frame_equal(matches, expected_matches, check_dtype=False, check_like=True)

    def setup_db_with_mock_data_rows(self):
        for crid in range(10000):
            new_allegation = DataAllegation(cr_id=crid)
            db.session.add(new_allegation)
        db.session.commit()
        db.session.close()

    def test_load_data_with_beat_id(self):
        testLoader = Loader()
        testLoader.load_into_db(expected_transformed_data_with_beat_id)

        queried_data_allegation = DataAllegation.query.all()
        assert (queried_data_allegation[0].beat_id == expected_transformed_data_with_beat_id.beat_id[0])

    def test_load_officer_data(self):
        testLoader = Loader()
        testLoader.load_into_db(expected_transformed_data_with_beat_id)
        queried_data_officerunknown = DataOfficerUnknown.query.all()
        assert (len(queried_data_officerunknown) == 6)

    def test_officer_allegation_dataframe_is_filled_when_load_officer_into_db(self):
        testLoader = Loader()
        df = pd.DataFrame([{
            "cr_id": '1008899',
            "number_of_officer_rows": 1,
            "beat_id": 433,
            "officer_race": ['White'],
            "officer_gender": ['M'],
            "officer_age": ['40-49'],
            "officer_years_on_force": ['0-4']
        }])
        for panda_row in df.itertuples():
            testLoader.load_officers_into_db(1, "1008899", panda_row)

        actual_data = testLoader.new_officer_allegation_data
        expected_data = pd.DataFrame([
            {
                "allegation_id": '1008899',
                "recc_finding": "NA",
                "recc_outcome": "NA",
                "final_finding": "NA",
                "final_outcome": "NA",
                "final_outcome_class": "NA",
            }
        ])
        assert_frame_equal(actual_data, expected_data, check_like=True)

    def test_unknown_officer_dataframe_is_filled_when_load_officer_into_db(self):
        testLoader = Loader()
        df = pd.DataFrame([{
            "cr_id": '1008899',
            "number_of_officer_rows": 1,
            "beat_id": 433,
            "officer_race": ['White'],
            "officer_gender": ['M'],
            "officer_age": ['40-49'],
            "officer_years_on_force": ['0-4']
        }])
        for panda_row in df.itertuples():
            testLoader.load_officers_into_db(1, "1008899", panda_row)

        actual_data = testLoader.new_officer_unknown_data
        expected_data = pd.DataFrame([
            {
                "data_officerallegation_id": 1,
                "age": '40-49',
                "race": 'White',
                "gender": 'M',
                "years_on_force": '0-4'
            }
        ])
        assert_frame_equal(actual_data, expected_data, check_like=True, check_dtype=False)
