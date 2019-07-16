import os
import pathlib

from werkzeug.datastructures import FileStorage

from invisible_flow.storage.storage_base import StorageBase


class LocalStorage(StorageBase):
    """Implementation of storage interface that saves files locally"""

    def store(self, filename, upload_file: FileStorage, path):
        dir_path = os.path.join('local_upload', path)

<<<<<<< Updated upstream
    def store(self, filename, upload_file: FileStorage, path):
        pathlib.Path(path).mkdir(exist_ok=True)
        with open(os.path.join(path, filename), 'wb') as file:
=======
        pathlib.Path(dir_path).mkdir(exist_ok=True, parents=True)
        with open(os.path.join(dir_path, filename), 'wb') as file:
>>>>>>> Stashed changes
            file.write(upload_file.read())
            file.close()

    def get(self, filename, path):
        with open(os.path.join(path, filename)) as file:
            return file.read()
