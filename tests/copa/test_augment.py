import os

import pandas as pd
from pandas.util.testing import assert_frame_equal

from invisible_flow.copa.augment import Augment
from tests.helpers.if_test_base import IFTestBase


class TestAugment:

    # def test_adding_augmented_copa_record_to_db(self):
    #     # using test file that is not actual copa that has been cleaned/transformed
    #     copa_split_csv = os.path.join(IFTestBase.resource_directory, 'copa_scraped_split.csv')
    #     df = pd.read_csv(copa_split_csv)
    #     clone_df = df
    #     db.create_all(bind=COPA_DB_BIND_KEY)
    #
    #     categories = df.loc[:, 'current_category'].unique()
    #
    #     for i in range(len(categories)):
    #         db.session.add(AllegationCategory(
    #             category=categories[i],
    #             category_code=i,
    #             cr_id='cats meow' + str(i)
    #         ))
    #         db.session.commit()
    #
    #     augmented = Augment().get_augmented_copa_data(copa_split_csv)
    #
    #     category_code_map = pd.DataFrame(
    #         AllegationCategory.query.with_entities(AllegationCategory.category, AllegationCategory.category_code)
    #     )
    #
    #     for category in categories:
    #         category_code = \
    #             category_code_map.loc[category_code_map['category'] == category]['category_code'].values[0]
    #         clone_df = clone_df.replace(category, category_code)
    #
    #     assert_frame_equal(augmented, clone_df)
    #     assert len(augmented) == len(df)
    #     assert len(clone_df) == len(df)

    def test_adding_augmented_copa_record_to_db_no_category_matches(self):
        copa_split_csv = os.path.join(IFTestBase.resource_directory, 'copa_scraped_split.csv')
        df = pd.read_csv(copa_split_csv)
        # db.drop_all()
        # db.create_all(bind=COPA_DB_BIND_KEY)

        augmented = Augment().get_augmented_copa_data(copa_split_csv)
        assert_frame_equal(augmented, df)
        assert len(augmented) == len(df)

    def test_adding_augmented_copa_record_to_db(self):
        # using test file that is not actual copa that has been  cleaned/transformed
        copa_csv_file = os.path.join(IFTestBase.resource_directory, 'copa_scraped_split.csv')
        original_dataframe = pd.read_csv(copa_csv_file)
        # db.create_all(bind=COPA_DB_BIND_KEY)

        log_no_column = original_dataframe.loc[:, 'log_no'].unique()
        categories_column = original_dataframe.loc[:, 'current_category'].unique()
        augmented_dataframe = Augment().get_augmented_copa_data(copa_csv_file)

        assert log_no_column.all()
        assert categories_column is not None
        assert augmented_dataframe is not None
        assert original_dataframe.equals(augmented_dataframe)

        print("orginal", original_dataframe.loc[:, 'current_category'], "/n")
        print("augmented", augmented_dataframe.loc[:, 'current_category'])
