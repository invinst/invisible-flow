from werkzeug.datastructures import FileStorage

from invisible_flow.storage.storage_base import StorageBase


class InMemoryStorage(StorageBase):
    def __init__(self):
        super().__init__()
        self.files = {}

    def store(self, filename, file: FileStorage, path):
        self.files[path] = {filename: file.stream.read()}
        # self.files[filename] = file.stream.read()

    def get(self, filename, path):
        return self.files[path][filename]

