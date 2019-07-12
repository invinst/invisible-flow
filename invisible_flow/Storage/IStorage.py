import abc

from werkzeug.datastructures import FileStorage


class IStorage(abc.ABC):
    """Interface to an implementation of storage communication"""

    def __init__(self):
        print("Instantiated as an interface!!!!!")

    @abc.abstractmethod
    def store(self, filename, file: FileStorage):
        pass