import os
from google.cloud import storage

from invisible_flow.storage import GCStorage, LocalStorage
from invisible_flow.storage.storage_base import StorageBase


class StorageFactory:

    @staticmethod
    def get_storage() -> StorageBase:
        if os.environ.get('ENVIRONMENT') == 'local':
            return LocalStorage()
        elif os.environ.get('ENVIRONMENT') == 'gae':
            gcs_client = storage.Client()
            return GCStorage(gcs_client)
        elif os.environ.get('ENVIRONMENT') == 'heroku':
            gcs_client = storage.Client()
            return GCStorage(gcs_client)
        else:
            raise Exception('Unable to determine the environment')
