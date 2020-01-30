import os
from datetime import datetime
from unittest import mock

from unittest.mock import call, patch
import pytest

from invisible_flow.copa.augment import Augment
from invisible_flow.copa.data_allegation import DataAllegation
from invisible_flow.constants import COPA_DB_BIND_KEY
from invisible_flow.copa.loader import Loader
from invisible_flow.storage import LocalStorage

from manage import db
from tests.helpers.if_test_base import IFTestBase


@patch('invisible_flow.app.GlobalsFactory.get_current_datetime_utc', lambda: datetime(2019, 3, 25, 5, 30, 50, 0))
class TestLoad:

    @pytest.fixture(autouse=True)
    def default_fixture(self):
        with patch('invisible_flow.app.StorageFactory.get_storage') as get_storage_mock:
            get_storage_mock.return_value = LocalStorage()
            yield get_storage_mock

    @pytest.fixture(autouse=True)
    def tear_down(self):
        db.session.close()

    @pytest.mark.skip
    def test_load_augmented_rows_no_collisions_with_db(self):
        db.drop_all()
        db.create_all(bind=COPA_DB_BIND_KEY)
        loader = Loader()
        copa_split_csv = os.path.join(IFTestBase.resource_directory, 'copa_scraped_split.csv')
        aug_copa_data = Augment().get_augmented_copa_data(copa_split_csv)
        loader.load_copa_db(aug_copa_data)
        assert len(aug_copa_data) == len(DataAllegation.query.all())
        assert len(loader.db_rows_added) == len(aug_copa_data)
        db.session.close()

    @pytest.mark.skip
    def test_where_all_augmented_data_matches_db_data(self):
        db.drop_all()
        db.create_all(bind=COPA_DB_BIND_KEY)
        loader = Loader()
        copa_split_csv = os.path.join(IFTestBase.resource_directory, 'copa_scraped_split.csv')
        aug_copa_data = Augment().get_augmented_copa_data(copa_split_csv)
        loader.load_copa_db(aug_copa_data)
        length_of_allegation = len(DataAllegation.query.all())
        loader.load_copa_db(aug_copa_data)
        assert length_of_allegation == len(DataAllegation.query.all())
        db.session.close()

    @pytest.mark.skip
    def test_where_augmented_data_is_partial_match(self, default_fixture):
        db.drop_all()
        db.create_all(bind=COPA_DB_BIND_KEY)
        loader = Loader()
        # number of partial matches in copa_scraped_modded
        partial_match_count = 3
        copa_modded = os.path.join(IFTestBase.resource_directory, 'copa_scraped_modded.csv')
        aug_mod_data = Augment().get_augmented_copa_data(copa_modded)
        with patch.object(LocalStorage, 'store_byte_string') as store_string_mock:
            loader.load_copa_db(aug_mod_data)
            assert partial_match_count == len(loader.partial_matches)
            calls = [
                call('changed_allegation.csv', mock.ANY, mock.ANY),
                call('error_notes.csv', mock.ANY, mock.ANY)
            ]
            store_string_mock.assert_has_calls(calls)
        db.session.close()

    @pytest.mark.skip
    def test_where_augmented_data_collides_and_error_notes_created(self, default_fixture):
        db.drop_all()
        db.create_all(bind=COPA_DB_BIND_KEY)
        loader = Loader()
        # number of partial matches in copa_scraped_modded
        partial_match_count = 3
        copa_modded = os.path.join(IFTestBase.resource_directory, 'copa_scraped_modded.csv')
        aug_mod_data = Augment().get_augmented_copa_data(copa_modded)
        loader.load_copa_db(aug_mod_data)
        assert len(loader.error_notes) >= partial_match_count
        assert len(loader.db_rows_added) == 10
        db.session.close()
