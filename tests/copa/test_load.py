# import os
# import pandas as pd
#
# from invisible_flow.copa.augment import Augment
# from invisible_flow.copa.data_allegation import Allegation
# from invisible_flow.constants import COPA_DB_BIND_KEY
# from invisible_flow.copa.loader import Loader
#
# from manage import db
# from tests.helpers.if_test_base import IFTestBase


class TestLoad:

    # def test_load_augmented_db(self):
    #     db.create_all(bind=COPA_DB_BIND_KEY)
    #     copa_split_csv = os.path.join(IFTestBase.resource_directory, 'copa_scraped_split.csv')
    #     aug_copa_data = Augment().get_augmented_copa_data(copa_split_csv)
    #     Loader().load_copa_db(aug_copa_data)
    #     assert len(aug_copa_data) == len(Allegation.query.all())

    # def test_where_all_augmented_data_matches_db_data(self):
    #     # db.drop_all()
    #     db.create_all(bind=COPA_DB_BIND_KEY)
    #     length_of_allegation = len(Allegation.query.all())
    #     copa_split_csv = os.path.join(IFTestBase.resource_directory, 'copa_scraped_split.csv')
    #     aug_copa_data = Augment().get_augmented_copa_data(copa_split_csv)
    #     Loader().load_copa_db(aug_copa_data)
    #     assert length_of_allegation == len(Allegation.query.all())

    def test_where_augmented_data_is_partial_match(self):
        pass
