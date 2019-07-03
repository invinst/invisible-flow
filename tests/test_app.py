import os
from io import BytesIO

import pytest

from invisible_flow.app import app
from invisible_flow.constants import FOIA_RESPONSE_UPLOAD_DIR, FOIA_RESPONSE_FIELD_NAME


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

    def test_foia_response_upload_returns_response_correctly(self):
        data = {
            'field': FOIA_RESPONSE_FIELD_NAME,
            'file': (BytesIO(b'some content'), '{}.csv'.format(FOIA_RESPONSE_FIELD_NAME))
        }

        response = self.test_client.post('/foia_response_upload', data=data, content_type='multipart/form-data')

        assert response.status_code == 200
        assert b'Success' in response.data

    def test_foia_response_upload_writes_to_uploads_dir(self):
        data = {
            'field': FOIA_RESPONSE_FIELD_NAME,
            'file': (BytesIO(b'some content'), '{}.csv'.format(FOIA_RESPONSE_FIELD_NAME))
        }

        self.test_client.post('/foia_response_upload', data=data, content_type='multipart/form-data')

        assert os.path.exists('{}{}'.format(FOIA_RESPONSE_UPLOAD_DIR, FOIA_RESPONSE_FIELD_NAME))
