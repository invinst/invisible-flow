import pytest
import validations


@pytest.mark.parametrize('filename', ['1.xls', '2.csv', '3.xlsx'])
def test_should_return_true_for_valid_extensions(filename):
    is_valid = validations.are_valid_file_extensions(filename)
    assert is_valid is True


@pytest.mark.parametrize('filename', ['1.doc', '2.txt', '3.dat'])
def test_should_return_false_for_invalid_extensions(filename):
    is_valid = validations.are_valid_file_extensions(filename)
    assert is_valid is False
