from io import BytesIO
from unittest import mock

import pytest

from invisible_flow.app import app
from invisible_flow.constants import FOIA_RESPONSE_FIELD_NAME
from invisible_flow.storage import InMemoryStorage


class TestInvisibleFlowApp:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.test_client = app.test_client(self)

    def test_index_route_should_render_correctly(self):
        response = self.test_client.get('/', content_type='html/text')

        assert response.status_code == 200
        assert b'FOIA' in response.data

    def test_index_route_throws_on_post_request(self):
        response = self.test_client.post('/', content_type='html/text')

        assert response.status_code == 405

    def test_foia_response_upload_uploads_to_memory(self):
        with mock.patch('invisible_flow.app.StorageFactory.get_storage') as storage_factory_mock:
            in_memory_storage = InMemoryStorage()
            storage_factory_mock.return_value = in_memory_storage

            file_name = '{}.csv'.format(FOIA_RESPONSE_FIELD_NAME)
            data = {
                'field': FOIA_RESPONSE_FIELD_NAME,
                'file': (BytesIO(b'some content'), file_name)
            }

            response = self.test_client.post('/foia_response_upload', data=data, content_type='multipart/form-data')

            actual_file = in_memory_storage.files.get(file_name)

            assert 1 == len(in_memory_storage.files)
            assert b'some content' == actual_file

            assert response.status_code == 200
            assert b'Success' in response.data

    @pytest.mark.parametrize('extension', ['txt', 'sh', 'py'])
    def test_unsupported_file_type_throw_on_post_request(self, extension):
        data = {
            'field': FOIA_RESPONSE_FIELD_NAME,
            'file': (BytesIO(b'some content'), '{}.{}'.format(FOIA_RESPONSE_FIELD_NAME, extension))
        }

        response = self.test_client.post('/foia_response_upload', data=data, content_type='multipart/form-data')

        assert response.status_code == 415
        assert b'Unsupported' in response.data
