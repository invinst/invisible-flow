import os

from werkzeug.datastructures import FileStorage

from invisible_flow.Storage.IStorage import IStorage


class GCStorage(IStorage):

    def store(self, filename, file: FileStorage):
        blob = self.bucket.blob(filename)
        blob.upload_from_string(file.stream.read1(), file.content_type)

    def __init__(self, gcs_client):
        self.gcs_client = gcs_client
        self.bucket = gcs_client.bucket(os.environ.get('GCS_BUCKET'))
        print("Instantiated for google cloud")
