import os

from google.cloud.storage import Client
from google.api_core.exceptions import GoogleAPICallError
from werkzeug.datastructures import FileStorage

from invisible_flow.storage.storage_base import StorageBase


class GCStorage(StorageBase):

    def store(self, filename, file: FileStorage, path):
        blob = self.bucket.blob(os.path.join(path, filename))
        blob.upload_from_string(file.stream.read1(), file.content_type)

    def get(self, filename, path):
        pass

    def store_metadata(self, filename: str, metadata_text: str) -> None:
        blob = self.bucket.blob(filename)
        try:
            blob.upload_from_string(metadata_text)
        except GoogleAPICallError as error:
            print(error)

    def __init__(self, gcs_client: Client):
        self.gcs_client = gcs_client
        self.bucket = gcs_client.bucket(os.environ.get('GCS_BUCKET'))
