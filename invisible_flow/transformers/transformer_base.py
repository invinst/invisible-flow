import abc

from typing import Tuple, List


class TransformerBase(abc.ABC):
    """Interface to an implementation of foia_upload transformation """

    """returns a tuple where the left value is the name of the new file, and the right value is
        the file content
    """
    @abc.abstractmethod
    def transform(self, response_type: str, file_content: str) -> List[Tuple[str, str]]:
        pass
