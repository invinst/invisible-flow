from datetime import datetime
from io import BytesIO
from unittest.mock import call, patch, MagicMock

import pytest
import pandas as pd
from flask.testing import FlaskClient

from invisible_flow.app import app
from invisible_flow.constants import FOIA_RESPONSE_FIELD_NAME, COPA_DB_BIND_KEY
from invisible_flow.storage import LocalStorage
from invisible_flow.storage.storage_factory import StorageFactory
from invisible_flow.transformers import CaseInfoAllegationsTransformer, CopaScrapeTransformer
from manage import db

from sqlalchemy.schema import DropTable
from sqlalchemy.ext.compiler import compiles


class TestInvisibleFlowApp:

    @pytest.fixture
    def client(self):
        app.testing = True
        test_client: FlaskClient = app.test_client()

        yield test_client
        # self.test_client: FlaskClient = app.test_client(self)

    # @pytest.mark.focus
    # def test_index_route_should_render_correctly(self, client):
    #     response = client.get('/', content_type='html/text')
    #
    #     assert response.status_code == 200

    def test_index_route_throws_on_post_request(self, client):
        response = client.post('/', content_type='html/text')

        assert response.status_code == 405

    @patch('invisible_flow.app.GlobalsFactory.get_current_datetime_utc', lambda: datetime(2019, 3, 25, 5, 30, 50, 0))
    def test_foia_response_upload_uploads_to_memory(self, client):
        # todo change this to a decorator
        with patch('invisible_flow.app.StorageFactory.get_storage') as storage_factory_mock, \
                patch('invisible_flow.app.TransformerFactory.get_transformer') as get_transformer_mock:
            storage_mock = LocalStorage()
            storage_factory_mock.return_value = storage_mock
            storage_mock.store = MagicMock()
            storage_mock.store_byte_string = MagicMock()

            get_transformer_mock.return_value = CaseInfoAllegationsTransformer()
            case_info_transformer_mock = get_transformer_mock()

            case_info_transformer_mock.transform = MagicMock()
            transform_mock = case_info_transformer_mock.transform
            transform_mock.return_value = [('accused', 'transformed content')]

            file_name = '{}.csv'.format(FOIA_RESPONSE_FIELD_NAME)
            data = {
                'foia_response': (BytesIO(b'some content'), file_name),
                'response_type': 'accused'
            }

            response = client.post('/foia_response_upload', data=data, content_type='multipart/form-data')

            assert response.status_code == 200
            assert b'Success' in response.data

            case_info_transformer_mock.transform.assert_called_with('accused', 'some content')

            calls = [
                call('accused.csv', b'some content', 'ui-2019-03-25_05-30-50/initial_data'),
                call('accused.csv', b'transformed content', 'ui-2019-03-25_05-30-50/transformed')
            ]
            storage_mock.store_byte_string.assert_has_calls(calls)
            # TODO test that xlsx is saved with ending

    @pytest.mark.parametrize('extension', ['txt', 'sh', 'py'])
    def test_unsupported_file_type_throw_on_post_request(self, extension, client):
        data = {
            'response_type': 'accused',
            'field': FOIA_RESPONSE_FIELD_NAME,
            'foia_response': (BytesIO(b'some content'), '{}.{}'.format(FOIA_RESPONSE_FIELD_NAME, extension))
        }

        response = client.post('/foia_response_upload', data=data, content_type='multipart/form-data')

        assert response.status_code == 415
        assert b'Unsupported' in response.data

    def test_copa_scrape_endpoint_responds(self, client):
        with patch.object(CopaScrapeTransformer, 'transform') as transform_mock, \
                patch.object(StorageFactory, 'get_storage'):
            transform_mock.return_value = [pd.DataFrame(), pd.DataFrame()]
            db.session.close()
            self.drop_with_cascade()
            db.create_all(bind=COPA_DB_BIND_KEY)

            response = client.get('/copa_scrape', content_type='html/text')

            assert response.status_code == 200
            assert b'Success' in response.data
            transform_mock.assert_called()

            self.drop_with_cascade()
            db.session.close()

    def drop_with_cascade(self):
        for table_name in db.metadata.tables.keys():
            DropTable(table_name)

    @compiles(DropTable, "postgresql")
    def _compile_drop_table(self, compiler, **kwargs):
        return compiler.visit_drop_table(self) + " CASCADE"
