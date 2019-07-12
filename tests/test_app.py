import os
from io import BytesIO
from unittest.mock import patch, MagicMock

import pytest
from google.cloud import storage

from invisible_flow.app import app
from invisible_flow.constants import FOIA_RESPONSE_FIELD_NAME


@patch('invisible_flow.app.storage.Client')
class TestInvisibleFlowApp:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.test_client = app.test_client(self)

    def test_index_route_should_render_correctly(self, gcs_client):

        response = self.test_client.get('/', content_type='html/text')

        assert response.status_code == 200
        assert b'FOIA' in response.data

    def test_index_route_throws_on_post_request(self, gcs_client):

        response = self.test_client.post('/', content_type='html/text')

        assert response.status_code == 405

    def test_foia_response_upload_returns_response_correctly(self, gcs_client):
        data = {
            'field': FOIA_RESPONSE_FIELD_NAME,
            'file': (BytesIO(b'some content'), '{}.csv'.format(FOIA_RESPONSE_FIELD_NAME))
        }

        response = self.test_client.post('/foia_response_upload', data=data, content_type='multipart/form-data')

        assert response.status_code == 200
        assert b'Success' in response.data

    @pytest.mark.parametrize('extension', ['csv', 'xlsx', 'xls'])
    def test_foia_response_upload_writes_to_uploads_dir(self, gcs_client, extension):
        data = {
            'field': FOIA_RESPONSE_FIELD_NAME,
            'file': (BytesIO(b'some content'), '{}.{}'.format(FOIA_RESPONSE_FIELD_NAME, extension))
        }

        gcs_client_mock = MagicMock(spec=storage.Client)
        gcs_client.return_value = gcs_client_mock

        bucket_blob_mock = MagicMock(spec=storage.bucket.Bucket)
        gcs_client_mock.bucket.return_value = bucket_blob_mock

        blob_mock = MagicMock(spec=storage.blob.Blob)
        bucket_blob_mock.blob.return_value = blob_mock

        self.test_client.post('/foia_response_upload', data=data, content_type='multipart/form-data')

        gcs_client_mock.bucket.assert_called_with(os.environ.get('GCS_BUCKET'))
        bucket_blob_mock.blob.assert_called_with(FOIA_RESPONSE_FIELD_NAME)
        blob_mock.upload_from_string.assert_called_once()

    @pytest.mark.parametrize('extension', ['txt', 'sh', 'py'])
    def test_unsupported_file_type_throw_on_post_request(self, gcs_client, extension):
        data = {
            'field': FOIA_RESPONSE_FIELD_NAME,
            'file': (BytesIO(b'some content'), '{}.{}'.format(FOIA_RESPONSE_FIELD_NAME, extension))
        }

        response = self.test_client.post('/foia_response_upload', data=data, content_type='multipart/form-data')

        assert response.status_code == 415
        assert b'Unsupported' in response.data
