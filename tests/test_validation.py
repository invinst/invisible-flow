import pytest
from invisible_flow import validation


@pytest.mark.parametrize('filename', ['1.xls', '2.csv', '3.xlsx'])
def test_should_return_true_for_valid_extensions(filename):
    assert validation.are_valid_file_extensions(filename)


@pytest.mark.parametrize('filename', ['1.doc', '2.txt', '3.dat'])
def test_should_return_false_for_invalid_extensions(filename):
    assert not validation.are_valid_file_extensions(filename)
