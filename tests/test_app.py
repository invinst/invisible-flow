
from invisible_flow.app import app


class TestInvisibleFlowApp:

    def test_index(self):
        test_client = app.test_client(self)
        response = test_client.get('/', content_type='html/text')

        assert response.status_code == 200
        assert response.data == b'Hello, World!'
