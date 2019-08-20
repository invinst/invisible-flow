import os
from logging import getLogger

from google.api_core.exceptions import GoogleAPICallError
from google.cloud.storage import Client

from invisible_flow.storage.storage_base import StorageBase

logger = getLogger(__name__)


class GCStorage(StorageBase):

    def __init__(self, gcs_client: Client):
        self.gcs_client = gcs_client
        self.bucket = gcs_client.bucket(os.environ.get('GCS_BUCKET'))

    def store_string(self, filename, file_content: str, path):
        blob = self.bucket.blob(os.path.join(path, filename))
        blob.upload_from_string(file_content, 'text/csv')

    def get(self, filename, path):
        return self.bucket.get_blob(path + filename)


    def store_metadata(self, filename: str, metadata_text: str) -> None:
        blob = self.bucket.blob(filename)
        try:
            blob.upload_from_string(metadata_text)
        except GoogleAPICallError as error:
            logger.error(f'Error uploading metadata to GCS. message:{error.message}')
