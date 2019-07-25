import abc

from werkzeug.datastructures import FileStorage


class StorageBase(abc.ABC):
    """Interface to an implementation of storage communication"""

    @abc.abstractmethod
    def store(self, filename, file: FileStorage, path):
        pass

    @abc.abstractmethod
    def get(self, filename, path):
        pass

    @abc.abstractmethod
    def store_string(self, filename, file_content: str, path: str):
        pass
