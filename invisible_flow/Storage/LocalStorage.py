from werkzeug.datastructures import FileStorage

from invisible_flow.Storage.IStorage import IStorage


class LocalStorage(IStorage):
    """Implementation of Storage interface that saves files locally"""

    def __init__(self):
        print("Instanted locally!!!!!!!")

    def store(self, filename, upload_file: FileStorage):
        with open(filename, 'wb') as file:
            file.write(upload_file.read())
            file.close()
