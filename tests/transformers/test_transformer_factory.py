import pytest

from invisible_flow.transformers import TransformerFactory


class TestTransformerFactory:
    def test_response_type_is_case_info(self):
        actual = TransformerFactory().get_transformer('case_info').__class__.__name__
        expected = 'CaseInfoAllegationsTransformer'
        assert actual == expected

    def test_response_type_is_investigator(self):
        actual = TransformerFactory().get_transformer('investigators').__class__.__name__
        expected = 'InvestigatorTransformer'
        assert actual == expected

    def test_response_type_is_complainant(self):
        actual = TransformerFactory().get_transformer('complainant').__class__.__name__
        expected = 'ComplainantTransformer'
        assert actual == expected


def test_response_type_is_invalid():
    with pytest.raises(Exception):
        TransformerFactory().get_transformer('No Match')
