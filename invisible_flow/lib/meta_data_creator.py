import json


class MetaDataCreator:

    def __init__(self, filename: str, commit: str, origin: str):

        if not filename or not isinstance(filename, str):
            raise ValueError('Output filename is invalid')
        if not commit or not isinstance(commit, str):
            raise ValueError('Invalid commit sha')
        if not origin or not isinstance(origin, str):
            raise ValueError('Invalid origin')

        self.filename = filename
        self.commit = commit
        self.origin = origin
        self.output_filename = f'{self.filename}.json'

    def build_and_return_dict(self):
        return {'sha': self.commit, 'origin': self.origin}

    def write_file_to_gcp(self, gcp_client):
        gcp_client.store_metadata(self.output_filename, json.dumps(self.build_and_return_dict()))
