from werkzeug.datastructures import FileStorage


class IStorage:
    """Interface to an implementation of storage communication"""

    def __init__(self):
        print("Instantiated as an interface!!!!!")

    def do_stuff(self):
        print("doing the stuff as an interface")

    def store(self, filename, file: FileStorage):
        raise NotImplementedError()
