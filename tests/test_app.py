
from invisible_flow.app import app


class TestInvisibleFlowApp:

    def test_index_route_should_render_correctly(self):
        test_client = app.test_client(self)

        response = test_client.get('/', content_type='html/text')

        assert response.status_code == 200
        assert b'FOIA' in response.data

    def test_index_route_throws_on_post_request(self):
        test_client = app.test_client(self)

        response = test_client.post('/', content_type='html/text')

        assert response.status_code == 405

