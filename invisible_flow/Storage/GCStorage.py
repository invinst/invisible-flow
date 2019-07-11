from invisible_flow.Storage.IStorage import IStorage


class GCStorage(IStorage):

    def __init__(self):
        print("Instantiated for google cloud")