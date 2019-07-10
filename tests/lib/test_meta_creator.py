import pytest

from invisible_flow.lib import meta_creator


def test_constructor_should_pass():
    assert True


def test_create_a_metadata_file():
    mc = meta_creator.MetaCreator

    assert mc.get_path_and_filename(mc, "Filename")
