import abc

from werkzeug.datastructures import FileStorage


class StorageBase(abc.ABC):
    """Interface to an implementation of storage communication"""

    @abc.abstractmethod
    def store(self, filename, file: FileStorage):
        pass


class InMemoryStorage(StorageBase):
    def __init__(self):
        super().__init__()
        self.files = {}

    def store(self, filename, file: FileStorage):
        self.files[filename] = file.stream.read()

    def getFile(self):
        return self.files[0]
