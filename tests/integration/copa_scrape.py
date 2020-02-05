import pytest
import os

from invisible_flow.copa.data_allegation import DataAllegation
from tests.helpers.if_test_base import IFTestBase
from unittest.mock import patch
from manage import db
from invisible_flow.constants import COPA_DB_BIND_KEY


class TestCopaSrapeIntegration:

    @pytest.fixture
    def getCopaData(self):
        copa_scraped_log_no_path = os.path.join(IFTestBase.resource_directory, 'copa_scraped_logno.csv')
        logno = open(copa_scraped_log_no_path).read()

        return logno

    @patch('invisible_flow.api.scrape_data', getCopaData)
    def test_copa_scrape_integration(self):
        db.session.close()
        db.drop_all()
        db.create_all(COPA_DB_BIND_KEY)

        self.initialize_database(db)

        # copa_scrape()

    def initialize_database(self, db):

        log_number_from_csv = ["1008899", "1087378", "1008915", "1009311", "1009355"]

        for log_no in log_number_from_csv:
            data_allegation = DataAllegation(
                cr_id=log_no
            )
            db.session.add(data_allegation)

        db.session.commit()
