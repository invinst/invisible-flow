import os

from google.cloud import storage
from invisible_flow.storage import GCStorage, InMemoryStorage, LocalStorage


class StorageFactory:

    @staticmethod
    def get_storage():
        if os.environ.get('ENVIRONMENT') == 'local':
            return LocalStorage()
        elif os.environ.get('ENVIRONMENT') == 'gae':
            gcs_client = storage.Client()
            return GCStorage(gcs_client)
        else:
            return InMemoryStorage()
