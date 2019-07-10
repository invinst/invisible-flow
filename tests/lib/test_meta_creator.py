import pytest
import os


from unittest.mock import patch, MagicMock
from google.cloud import storage

from invisible_flow.lib import meta_creator




def test_constructor_should_have_nonempty_string():
    mc = meta_creator.MetaCreator("path")

    assert mc.path.strip()


# def test_should_contain_dict_values():
#     key_value = {'sha': "821931298318", "origin": "UI/FOIA"}
#     mc = meta_creator.MetaCreator(key_value)
#     expected = "821931298318"
#     actual = mc.create_meta_data_json()
#
#     assert actual == expected

def test_output_filename_is_original_filename_with_json_ext():
    mc = meta_creator.MetaCreator("filename", "sha", "origin")
    assert mc.output_filename == "filename.json"


def test_build_dict_contains_origin_and_sha():
    mc = meta_creator.MetaCreator("filename", "sha", "origin")
    expected_sha = "sha"
    expected_origin = "origin"
    dic = mc.build_and_return_dict()
    actual_sha = dic["sha"]
    actual_origin = dic["origin"]

    assert expected_origin == actual_origin
    assert expected_sha == actual_sha


def test_json_file_exists_after_writing():
    mc = meta_creator.MetaCreator("filename", "sha", "origin")
    mcw = meta_creator.MetaCreatorWriter(mc)

    mcw.write_file_locally()
    f = open(mc.output_filename, "r")
    assert f.mode == "r"


def test_json_file_write_to_gcp_called():
    gcs_client_mock = MagicMock(speç=storage.Client)

    bucket_blob_mock = MagicMock(spec=storage.bucket.Bucket)
    gcs_client_mock.get_bucket.return_value = bucket_blob_mock

    blob_mock = MagicMock(spec=storage.blob.Blob)
    bucket_blob_mock.get_blob.return_value = blob_mock

    mc = meta_creator.MetaCreator("filename", "sha", "origin")
    mcw = meta_creator.MetaCreatorWriter(mc)

    # gcs_client_mock.bucket.assert_called_with(os.environ.get('GCS_BUCKET'))
    # bucket_blob_mock.blob.assert_called_with("")

    assert mcw.write_file_to_gcp(gcs_client_mock, "test_bucket")
    blob_mock.upload_from_string.assert_called_once()

