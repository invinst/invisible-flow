import os
import json
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
            creds = os.environ.get('TEMP')
            with open('googleCred.json', 'w') as f:  # writing JSON object
                json.dump(creds, f)
            gcs_client = storage.Client.from_service_account_json('googleCred.json')
            return GCStorage(gcs_client)
        else:
            raise Exception('Unable to determine the environment')
