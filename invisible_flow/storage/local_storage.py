from werkzeug.datastructures import FileStorage

from invisible_flow.storage.storage_base import StorageBase


class LocalStorage(StorageBase):
    """Implementation of storage interface that saves files locally"""

    def __init__(self):
        print("Instantiated locally!!!!!!!")

    def store(self, filename, upload_file: FileStorage):
        with open(filename, 'wb') as file:
            file.write(upload_file.read())
            file.close()
