import abc


class TransformerBase(abc.ABC):
    """Interface to an implementation of foia_upload transformation """

    @abc.abstractmethod
    def transform(self, response_type, file_content: str):
        pass
