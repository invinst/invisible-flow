import os

from invisible_flow.transformers.accused_transformer import AccusedTransformer

from tests.helpers.if_test_base import IFTestBase


class TestAccusedTransformer:

    def test_transform_head(self):
        transformer = AccusedTransformer()
        head_accused_path = os.path.join(IFTestBase.resource_directory, 'accused_head.csv')
        allegationcategory_accused_path = os.path.join(IFTestBase.resource_directory, 'accused_allegationcategory.csv')
        officer_accused_path = os.path.join(IFTestBase.resource_directory, 'accused_officer.csv')
        officerbadgenumber_accused_path = os.path.join(IFTestBase.resource_directory, 'accused_officerbadgenumber.csv')
        policeunit_accused_path = os.path.join(IFTestBase.resource_directory, 'accused_policeunit.csv')

        with open(head_accused_path) as file:
            expected_result = [
                ('allegationcategory', open(allegationcategory_accused_path).read()),
                ('officer', open(officer_accused_path).read()),
                ('officerbadgenumber', open(officerbadgenumber_accused_path).read()),
                ('policeunit', open(policeunit_accused_path).read())
            ]
            actual_result = transformer.transform('accused', file.read())
            assert actual_result == expected_result
