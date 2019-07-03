import os
from io import BytesIO

import pytest

from invisible_flow.app import app
from invisible_flow.constants import FOIA_RESPONSE_UPLOAD_DIR, FOIA_RESPONSE_FIELD_NAME


class TestInvisibleFlowApp:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.test_client = app.test_client(self)

    def create_data(self, extension):
        return {
            'field': FOIA_RESPONSE_FIELD_NAME,
            'file': (BytesIO(b'some content'), '{}.{}'.format(FOIA_RESPONSE_FIELD_NAME, extension))
        }

    def client_post(self, d):
        return self.test_client.post('/foia_response_upload', data=d, content_type='multipart/form-data')

    def test_index_route_should_render_correctly(self):

        response = self.test_client.get('/', content_type='html/text')

        assert response.status_code == 200
        assert b'FOIA' in response.data

    def test_index_route_throws_on_post_request(self):

        response = self.test_client.post('/', content_type='html/text')

        assert response.status_code == 405

    def test_foia_response_upload_returns_response_correctly(self):

        response = self.client_post(self.create_data('csv'))

        assert response.status_code == 200
        assert b'Success' in response.data

    @pytest.mark.parametrize('extension', ['csv', 'xlsx', 'xls'])
    def test_foia_response_upload_writes_to_uploads_dir(self, extension):

        self.client_post(self.create_data(extension))

        assert os.path.exists('{}{}'.format(FOIA_RESPONSE_UPLOAD_DIR, FOIA_RESPONSE_FIELD_NAME))

    @pytest.mark.parametrize('extension', ['txt', 'sh', 'py'])
    def test_unsupported_file_type_throw_on_post_request(self, extension):

        response = self.client_post(self.create_data(extension))

        assert response.status_code == 415
        assert b'Unsupported' in response.data
