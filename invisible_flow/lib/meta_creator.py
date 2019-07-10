import json, os
from google.cloud import storage

class MetaCreator:
    commit = None
    origin = None
    filename = None
    output_filename = None

    def __init__(self, filename, sha, origin):
        self.filename = filename
        self.commit = sha
        self.origin = origin
        self.output_filename = self.filename + ".json"

    #  def output_meta_data_json(self):

    def build_and_return_dict(self):
        return {"sha": self.commit, "origin": self.origin}


class MetaCreatorWriter:
    meta_creator = None

    def __init__(self, meta_creator):
        self.meta_creator = meta_creator

    def write_file_locally(self):
        f = open(self.meta_creator.output_filename, "w+")
        f.write(json.dumps(self.meta_creator.build_and_return_dict()))

    def write_file_to_gcp(self, gcp_client, bucket_name):

        bucket = gcp_client.get_bucket(bucket_name)
        blob = bucket.get_blob(self.meta_creator.output_filename)
        json_string = json.dumps(self.meta_creator.build_and_return_dict())
        blob.upload_from_string(json_string)
        return self.verify(self.meta_creator.output_filename, bucket, json_string)

    def verify(self, filename, bucket, json_string):

        blob = bucket.get_blob(filename)
        return json_string == blob.download_as_string()
