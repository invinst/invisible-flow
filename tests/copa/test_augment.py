import os
from invisible_flow.copa.augment import Augment
from tests.helpers.if_test_base import IFTestBase


class TestAugment:

    def test_adding_copa_record_to_db_works(self):
        copa_split_csv = os.path.join(IFTestBase.resource_directory, 'copa_scraped_split.csv')
        Augment().get_transform_copa_data(copa_split_csv)
