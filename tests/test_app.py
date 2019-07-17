from datetime import datetime
from io import BytesIO
from unittest import mock
from unittest.mock import patch, MagicMock

import pytest
from flask.testing import FlaskClient

from invisible_flow.app import app
from invisible_flow.constants import FOIA_RESPONSE_FIELD_NAME
from invisible_flow.storage import LocalStorage


class TestInvisibleFlowApp:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.test_client: FlaskClient = app.test_client(self)

    def test_index_route_should_render_correctly(self):
        response = self.test_client.get('/', content_type='html/text')

        assert response.status_code == 200
        assert b'FOIA' in response.data

    def test_index_route_throws_on_post_request(self):
        response = self.test_client.post('/', content_type='html/text')

        assert response.status_code == 405

    @patch('invisible_flow.app.GlobalsFactory.get_current_datetime_utc', lambda: datetime(2019, 3, 25, 5, 30, 50, 0))
    def test_foia_response_upload_uploads_to_memory(self):
        # todo change this to a decorator
        with mock.patch('invisible_flow.app.StorageFactory.get_storage') as storage_factory_mock:
            storage_mock = LocalStorage()
            storage_factory_mock.return_value = storage_mock
            storage_mock.store = MagicMock()

            file_name = '{}.csv'.format(FOIA_RESPONSE_FIELD_NAME)
            data = {
                'foia_response': (BytesIO(b'some content'), file_name),
                'response_type': 'accused'
            }

            response = self.test_client.post('/foia_response_upload', data=data, content_type='multipart/form-data')

            assert response.status_code == 200
            assert b'Success' in response.data

            storage_mock.store.assert_called_with('accused.csv', mock.ANY, 'ui-2019-03-25_05-30-50/initial_data')

            # TODO test that xlsx is saved with ending

    @pytest.mark.focus
    @pytest.mark.parametrize('extension', ['txt', 'sh', 'py'])
    def test_unsupported_file_type_throw_on_post_request(self, extension):
        data = {
            'response_type': 'accused',
            'field': FOIA_RESPONSE_FIELD_NAME,
            'foia_response': (BytesIO(b'some content'), '{}.{}'.format(FOIA_RESPONSE_FIELD_NAME, extension))
        }

        response = self.test_client.post('/foia_response_upload', data=data, content_type='multipart/form-data')

        assert response.status_code == 415
        assert b'Unsupported' in response.data
