import os
from io import BytesIO
from unittest import mock
from unittest.mock import MagicMock

from google.cloud import storage
from werkzeug.datastructures import FileStorage

from invisible_flow.storage.gcs_storage import GCStorage
from invisible_flow.storage.local_storage import LocalStorage
from invisible_flow.constants import FOIA_RESPONSE_FIELD_NAME


class TestLocalStorage:
    subject = LocalStorage()
    fake_file_storage = FileStorage(stream=BytesIO(b'Some content'))

    def test_store_does_not_throw_exception_when_used(self):
        self.subject.store('Blah', self.fake_file_storage)
        os.remove('Blah')

    def test_store_writes_file_locally(self):
        self.subject.store(FOIA_RESPONSE_FIELD_NAME, self.fake_file_storage)
        assert os.path.exists(FOIA_RESPONSE_FIELD_NAME)
        os.remove(FOIA_RESPONSE_FIELD_NAME)


class TestGCStorage:
    fake_file_storage = FileStorage(stream=BytesIO(b'Some content'), content_type='csv')

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

            subject.store(FOIA_RESPONSE_FIELD_NAME, self.fake_file_storage)

            # Bucket should be instantiated with the bucket url
            subject.gcs_client.bucket.assert_called_with("gcs-bucket-url")
            subject.bucket.blob.assert_called_with(FOIA_RESPONSE_FIELD_NAME)

            # Return value of blob call is a mock, so we can assert on it
            subject.bucket.blob.return_value.upload_from_string.assert_called_with(b'Some content', 'csv')
