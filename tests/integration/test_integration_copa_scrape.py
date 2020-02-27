import os
from datetime import datetime
from unittest.mock import patch

import pytest

from invisible_flow.app import copa_scrape
from invisible_flow.copa.data_allegation import DataAllegation
from invisible_flow.copa.data_officer_allegation import DataOfficerAllegation
from invisible_flow.storage import LocalStorage
from invisible_flow.storage.storage_factory import StorageFactory
from manage import db
from tests.helpers.if_test_base import IFTestBase


class TestCopaSrapeIntegration:

    @pytest.fixture
    def get_copa_data(self):
        copa_scraped_log_no_path = os.path.join(IFTestBase.resource_directory, 'copa_scraped_logno.csv')
        logno = open(copa_scraped_log_no_path, 'rb').read()

        yield logno

    def initialize_database(self, db):
        db.session.query(DataAllegation).delete()
        db.session.query(DataOfficerAllegation).delete()
        db.session.commit()

        log_number_from_csv = ["1008899", "1087378", "1008915", "1009311", "1009355"]

        for log_no in log_number_from_csv:
            data_allegation = DataAllegation(
                cr_id=log_no
            )
            db.session.add(data_allegation)

        db.session.commit()

    @patch('invisible_flow.app.GlobalsFactory.get_current_datetime_utc', lambda: datetime(2019, 3, 25, 5, 30, 50, 0))
    def test_copa_scrape_integration(self, get_copa_data):
        with patch.object(StorageFactory, 'get_storage') as storage_mock, \
                patch('invisible_flow.app.scrape_data') as scrape_mock:

            scrape_mock.return_value = get_copa_data

            storage_mock.return_value = LocalStorage()

            db.session.close()

            self.initialize_database(db)

            copa_scrape()

            match_data_file_contents = LocalStorage().get('match_data.csv', "COPA_SCRAPE-2019-03-25_05-30-50")
            new_data_file_contents = LocalStorage().get('new_data.csv', "COPA_SCRAPE-2019-03-25_05-30-50")

            expected_match_data_file_contents = open(os.path.join(IFTestBase.resource_directory,
                                                                  'expected_match_copa_data.csv')).read()
            expected_new_data_file_contents = open(os.path.join(IFTestBase.resource_directory,
                                                                'expected_new_copa_data.csv')).read()

            entry_from_db = DataAllegation.query.get('1087387')
            number_of_rows_in_db = DataAllegation.query.count()

            assert(new_data_file_contents == expected_new_data_file_contents)
            assert(match_data_file_contents == expected_match_data_file_contents)

            assert(entry_from_db is not None)
            assert(number_of_rows_in_db == 149)

            db.session.query(DataAllegation).delete()
            db.session.query(DataOfficerAllegation).delete()
            db.session.commit()
            db.session.close()

            local_upload_dir = LocalStorage().local_upload_directory

            os.remove(os.path.join(local_upload_dir, "COPA_SCRAPE-2019-03-25_05-30-50", 'match_data.csv'))
            os.remove(os.path.join(local_upload_dir, "COPA_SCRAPE-2019-03-25_05-30-50", 'new_data.csv'))

            os.rmdir(os.path.join(local_upload_dir, "COPA_SCRAPE-2019-03-25_05-30-50"))
