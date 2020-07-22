from datetime import datetime

import pytest
import os

from invisible_flow.app import copa_scrape
from invisible_flow.copa.data_allegation import DataAllegation
from invisible_flow.copa.existing_crid import ExistingCrid
from invisible_flow.storage import LocalStorage
from invisible_flow.storage.storage_factory import StorageFactory
from invisible_flow.globals_factory import GlobalsFactory  # noqa: F401
from tests.helpers.if_test_base import IFTestBase
from unittest.mock import patch
from manage import db
from invisible_flow.constants import COPA_DB_BIND_KEY


class TestCopaSrapeIntegration:

    @pytest.fixture
    def get_copa_data(self):
        copa_scraped_log_no_path = os.path.join(IFTestBase.resource_directory, 'copa_scraped_logno.csv')
        logno = open(copa_scraped_log_no_path, 'rb').read()

        yield logno

    @pytest.fixture
    def get_copa_data_demographics(self):
        copa_scraped_log_no_path = os.path.join(IFTestBase.resource_directory, 'test_copa_scraped_allegation_data.csv')
        copa_data = open(copa_scraped_log_no_path, 'rb').read()

        yield copa_data

    @pytest.fixture
    def get_copa_officer_data_demographics(self):
        copa_scraped_log_no_path = os.path.join(IFTestBase.resource_directory, 'new_officer_allegation_data.csv')
        # copa_scraped_log_no_path = os.path.join(IFTestBase.resource_directory, 'test_copa_scraped_officer_data.csv')
        copa_data = open(copa_scraped_log_no_path, 'rb').read()

        yield copa_data

    @pytest.fixture
    def get_copa_crids(self):
        copa_scraped_log_no_path = os.path.join(IFTestBase.resource_directory, 'test_copa_scraped_crids.csv')
        copa_data = open(copa_scraped_log_no_path, 'rb').read()

        yield copa_data

    def initialize_database(self, db):
        log_number_from_csv = ["1008899", "1087378", "1008915", "1009311", "1009355"]
        existing_crids_str = "1008899,1087378,1008915,1009311,1009355"

        for log_no in log_number_from_csv:
            data_allegation = DataAllegation(cr_id=log_no, beat_id="111")
            db.session.add(data_allegation)

        existing_crids = ExistingCrid(existing_crids=existing_crids_str)
        db.session.add(existing_crids)

        db.session.commit()
    @pytest.mark.focus
    @patch('invisible_flow.app.GlobalsFactory.get_current_datetime_utc', lambda: datetime(2019, 3, 25, 5, 30, 50, 0))
    def test_copa_scrape_integration(self, get_copa_data_demographics,
                                     get_copa_officer_data_demographics, get_copa_crids):
        with patch.object(StorageFactory, 'get_storage') as storage_mock, \
                patch('invisible_flow.app.scrape_allegation_data') as scrape_mock, \
                patch('invisible_flow.app.scrape_officer_data') as officer_scrape_mock, \
                patch('invisible_flow.app.scrape_crids') as crid_scrape_mock:
            scrape_mock.return_value = get_copa_data_demographics
            officer_scrape_mock.return_value = get_copa_officer_data_demographics
            crid_scrape_mock.return_value = get_copa_crids

            storage_mock.return_value = LocalStorage()

            db.session.close()
            db.drop_all()
            db.create_all(COPA_DB_BIND_KEY)

            self.initialize_database(db)

            copa_scrape()

            existing_allegation_file_contents = LocalStorage().get('existing_allegation_data.csv',
                                                                   "COPA_SCRAPE-2019-03-25_05-30-50")
            new_allegation_file_contents = LocalStorage().get(
                'new_allegation_data.csv', "COPA_SCRAPE-2019-03-25_05-30-50")

            expected_existing_allegation_file_contents = open(os.path.join(
                IFTestBase.resource_directory, 'expected_existing_allegation_data.csv')).read()

            expected_new_allegation_data = open(os.path.join(IFTestBase.resource_directory,
                                                             'expected_new_allegation_data.csv')).read()

            entry_from_db = DataAllegation.query.get('1087387')
            number_of_rows_in_db = DataAllegation.query.count()

            # tests > helpers > resources (can find csv contents used in these tests
            # new_data & existing_data should show up in local_upload_folder
            assert(existing_allegation_file_contents == expected_existing_allegation_file_contents)
            assert(new_allegation_file_contents == expected_new_allegation_data)

            assert(entry_from_db is not None)
            assert(number_of_rows_in_db == 151)

            local_upload_dir = LocalStorage().local_upload_directory

            os.remove(os.path.join(local_upload_dir, "COPA_SCRAPE-2019-03-25_05-30-50", 'existing_allegation_data.csv'))
            os.remove(os.path.join(local_upload_dir, "COPA_SCRAPE-2019-03-25_05-30-50", 'new_allegation_data.csv'))
            os.remove(os.path.join(local_upload_dir, "COPA_SCRAPE-2019-03-25_05-30-50", 'existing_officer_data.csv'))
            os.remove(os.path.join(local_upload_dir, "COPA_SCRAPE-2019-03-25_05-30-50", 'new_officer_allegation_data.csv'))

            os.rmdir(os.path.join(local_upload_dir, "COPA_SCRAPE-2019-03-25_05-30-50"))
