from io import BytesIO
from unittest import mock
from unittest.mock import MagicMock

from google.cloud import storage
from werkzeug.datastructures import FileStorage

from invisible_flow.storage import GCStorage


class TestGCStorage:
    fake_file_storage = FileStorage(stream=BytesIO(b'Some content'), content_type='csv')
    fake_file_contents = "I love dem tacos very much"

    def create_gcs_storage(self):
        gcs_client_mock = MagicMock(spec=storage.Client)

        bucket_blob_mock = MagicMock(spec=storage.bucket.Bucket)
        gcs_client_mock.bucket.return_value = bucket_blob_mock

        blob_mock = MagicMock(spec=storage.blob.Blob)
        bucket_blob_mock.blob.return_value = blob_mock

        return GCStorage(gcs_client_mock)

    def test_store_sends_files_to_gcp(self):
        with mock.patch('invisible_flow.storage.gcs_storage.os.environ.get') as os_environ_get_mock:
            os_environ_get_mock.return_value = 'gcs-bucket-url'
            subject = self.create_gcs_storage()

            subject.store('some-file.csv', self.fake_file_storage, 'some/path')

            # Bucket should be instantiated with the bucket url
            subject.gcs_client.bucket.assert_called_with("gcs-bucket-url")
            subject.bucket.blob.assert_called_with('some/path/some-file.csv')

            # Return value of blob call is a mock, so we can assert on it
            subject.bucket.blob.return_value.upload_from_string.assert_called_with(b'Some content', 'csv')

    def test_store_sends_file_contents_string_to_gcp(self):
        with mock.patch('invisible_flow.storage.gcs_storage.os.environ.get') as os_environ_get_mock:
            os_environ_get_mock.return_value = 'gcs-bucket-url'
            subject = self.create_gcs_storage()

            subject.store_string('some-file.csv', self.fake_file_contents, 'some/path')

            # Bucket should be instantiated with the bucket url
            subject.gcs_client.bucket.assert_called_with("gcs-bucket-url")
            subject.bucket.blob.assert_called_with('some/path/some-file.csv')

            # Return value of blob call is a mock, so we can assert on it
            subject.bucket.blob.return_value.upload_from_string.assert_called_with(
                'I love dem tacos very much', 'text/csv')
