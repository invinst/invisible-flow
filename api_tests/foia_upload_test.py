import requests


class TestFoiaUpload:
    foia_upload_url = 'http://127.0.0.1:5000/foia_response_upload'

    # in the future this should support excel file types
    def test_post_request_file_must_be_a_valid_file_type(self):
        valid_file = {'foia_response': ('blah.csv', open('../tests/helpers/resources/accused_single_row.csv'))}
        response = requests.post(
            self.foia_upload_url,
            files=valid_file, data={'response_type': 'accused'}
        )

        assert 200 <= response.status_code <= 299
        assert 'Success' in response.text

    def test_post_request_must_contain_a_file(self):
        response = requests.post(
            self.foia_upload_url, data={'response_type': 'accused'}
        )

        assert response.status_code == 400
        assert 'No file with name foia_response was uploaded' in response.text

    def test_post_request_must_specify_response_type(self):
        valid_file = {'foia_response': ('blah.csv', open('../tests/helpers/resources/accused_single_row.csv'))}
        response = requests.post(
            self.foia_upload_url,
            files=valid_file
        )

        assert response.status_code == 400
        assert 'No response type for the file was specified' in response.text
