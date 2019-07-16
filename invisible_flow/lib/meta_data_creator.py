import json


class MetaDataCreator:
    commit = None
    origin = None
    filename = None
    output_filename = None

    def __init__(self, filename, commit, origin):

        if not filename or not isinstance(filename, str):
            raise ValueError('Output filename is invalid')
        if not commit or not isinstance(commit, str):
            raise ValueError('Invalid commit sha')
        if not origin or not isinstance(origin, str):
            raise ValueError('Invalid origin')

        self.filename = filename
        self.commit = commit
        self.origin = origin
        self.output_filename = '{}.json'.format(self.filename)

    #  def output_meta_data_json(self):

    def build_and_return_dict(self):
        return {'sha': self.commit, 'origin': self.origin}

    def write_file_to_gcp(self, gcp_client):
        gcp_client.store_metadata(self.output_filename, json.dumps(self.build_and_return_dict()))
