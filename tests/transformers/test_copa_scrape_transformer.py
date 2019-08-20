import os
import pandas as pd
from mock import patch

from invisible_flow.storage import LocalStorage
from invisible_flow.transformers.copa_scrape_transformer import CopaScrapeTransformer

from tests.helpers.if_test_base import IFTestBase


class TestCopaScrapeTransformer(IFTestBase):

    def test_split_passes(self):
        self.copa = False
        self.no_copa = False
        transformer = CopaScrapeTransformer()
        raw_data = transformer.split()
        for row in raw_data['copa']:
            if row['assignment'] != 'COPA':
                self.copa = True

        for row in raw_data['no_copa']:
            if row['assignment'] == 'COPA':
                self.no_copa = True

        assert not self.copa
        assert not self.no_copa

    def test_split_fails(self):
        self.copa = False
        self.no_copa = False
        transformer = CopaScrapeTransformer()
        raw_data = transformer.split()
        raw_data['copa'].append({'assignment': 'MOOOOOOOOOO'})
        raw_data['no_copa'].append({'assignment': 'COPA'})
        for row in raw_data['copa']:
            if row['assignment'] != 'COPA':
                self.copa = True

        for row in raw_data['no_copa']:
            if row['assignment'] == 'COPA':
                self.no_copa = True

        assert self.copa
        assert self.no_copa

    def test_convert_to_csv(self):
        copa_scraped_split = os.path.join(IFTestBase.resource_directory, 'copa_scraped_split.json')
        copa_split_csv = os.path.join(IFTestBase.resource_directory, 'copa_scraped_split.csv')
        no_copa_split_csv = os.path.join(IFTestBase.resource_directory, 'no_copa_scraped_split.csv')
        transformer = CopaScrapeTransformer()
        raw_data = pd.read_json(open(copa_scraped_split).read(), orient='records')
        actual = transformer.convert_to_csv(raw_data)
        assert actual['copa'] == open(copa_split_csv).read()
        assert actual['no_copa'] == open(no_copa_split_csv).read()

    def test_upload_to_gcs(self):
        copa_split_csv = os.path.join(IFTestBase.resource_directory, 'copa_scraped_split.csv')
        no_copa_split_csv = os.path.join(IFTestBase.resource_directory, 'no_copa_scraped_split.csv')
        mock_converted_output = {"copa": open(copa_split_csv).read(), "no_copa": open(no_copa_split_csv).read()}
        with patch('invisible_flow.app.StorageFactory.get_storage') as get_storage_mock:
            with patch.object(LocalStorage, 'store_string') as mock:
                get_storage_mock.return_value = LocalStorage()
                transformer = CopaScrapeTransformer()
                transformer.upload_to_gcs(mock_converted_output)
        mock.assert_called()
