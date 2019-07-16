import pytest

from unittest.mock import MagicMock
from google.cloud import storage
from invisible_flow.storage.gcs_storage import GCStorage

from invisible_flow.lib import meta_data_creator


def test_invalid_filename_throw_value_error():
    with pytest.raises(ValueError):
        meta_data_creator.MetaDataCreator(1, 'sha', 'origin')


def test_invalid_commit_throw_value_error():
    with pytest.raises(ValueError):
        meta_data_creator.MetaDataCreator('filename', {}, 'origin')


def test_invalid_origin_throw_value_error():
    with pytest.raises(ValueError):
        meta_data_creator.MetaDataCreator('filename', 'sha', '')


def test_output_filename_is_original_filename_with_json_ext():
    mc = meta_data_creator.MetaDataCreator('filename', 'sha', 'origin')
    assert mc.output_filename == 'filename.json'


def test_build_dict_contains_origin_and_sha():
    mc = meta_data_creator.MetaDataCreator('filename', 'sha', 'origin')
    expected_sha = 'sha'
    expected_origin = 'origin'
    dic = mc.build_and_return_dict()
    actual_sha = dic['sha']
    actual_origin = dic['origin']

    assert expected_origin == actual_origin
    assert expected_sha == actual_sha


def test_json_file_write_to_gcp_called():
    gcs_client_mock = MagicMock(speç=GCStorage)

    bucket_blob_mock = MagicMock(spec=storage.bucket.Bucket)
    gcs_client_mock.get_bucket.return_value = bucket_blob_mock

    blob_mock = MagicMock(spec=storage.blob.Blob)
    bucket_blob_mock.blob.return_value = blob_mock

    mc = meta_data_creator.MetaDataCreator('filename', 'sha', 'origin')

    mc.write_file_to_gcp(gcs_client_mock)

    gcs_client_mock.store_metadata.assert_called_once()
