from unittest.mock import patch

import pytest
from flask.testing import FlaskClient

from invisible_flow.app import app
from invisible_flow.constants import COPA_DB_BIND_KEY
from invisible_flow.storage.storage_factory import StorageFactory
from manage import db

from sqlalchemy.schema import DropTable
from sqlalchemy.ext.compiler import compiles


class TestInvisibleFlowApp:

    @pytest.fixture
    def client(self):
        app.testing = True
        test_client: FlaskClient = app.test_client()

        yield test_client

    def test_index_route_throws_on_post_request(self, client):
        response = client.post('/', content_type='html/text')

        assert response.status_code == 405

    def drop_with_cascade(self):
        for table_name in db.metadata.tables.keys():
            DropTable(table_name)

    @compiles(DropTable, "postgresql")
    def _compile_drop_table(self, compiler, **kwargs):
        return compiler.visit_drop_table(self) + " CASCADE"

    def test_copa_scrape(self, client):
        with patch.object(StorageFactory, 'get_storage'):
            db.session.close()
            db.drop_all()
            db.create_all(bind=COPA_DB_BIND_KEY)

            response = client.get('/copa_scrape', content_type='html/text')
            assert response.status_code == 200
            assert b'Success' in response.data
