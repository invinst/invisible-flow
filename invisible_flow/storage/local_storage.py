import os
import pathlib

from invisible_flow.storage.storage_base import StorageBase


class LocalStorage(StorageBase):
    """Implementation of storage interface that saves files locally"""

    package_directory = os.path.dirname(os.path.abspath(__file__))
    local_upload_directory = os.path.join(package_directory, '..', 'local_upload')

    def store_byte_string(self, filename, file_content: bytes, path: str):
        dir_path = os.path.join(self.local_upload_directory, path)

        pathlib.Path(dir_path).mkdir(exist_ok=True, parents=True)
        with open(os.path.join(dir_path, filename), 'wb') as file:
            file.write(file_content)
            file.close()

    def store_string_with_type(self, filename, file_content: bytes, path: str, file_type: str):
        self.store_byte_string(filename, file_content, path)

    def get(self, filename, path):
        try:
            with open(os.path.join(self.local_upload_directory, path, filename)) as file:
                return file.read()
        except FileNotFoundError:
            print('file not found error')
            return None
