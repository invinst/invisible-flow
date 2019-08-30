import os
from invisible_flow.copa.augment import Augment
from tests.helpers.if_test_base import IFTestBase


class TestAugment:

    def test_adding_augmented_copa_record_to_db(self):
        # using test file that is not actual copa that has been cleaned/transformed
        copa_split_csv = os.path.join(IFTestBase.resource_directory, 'copa_scraped_split.csv')

        # TODO fix up tests, verify that with a lits of AllegationCategories that has at least
        # one category/category_code pair that exists in our current csv
        # verify dataframe returned has replaced those values correctly

        # for experiments and testing only
        # for i in range(len(categories)):
        #     db.session.add(AllegationCategory(
        #         category=categories[i],
        #         category_code=i,
        #         cr_id='cats meow' + str(i)
        #     ))
        #     db.session.commit()
        # for experiments and testing only
        Augment().get_augmented_copa_data(copa_split_csv)

    # TODO add test for when no AllegationCategories match categories in list