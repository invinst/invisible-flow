import os

from io import BytesIO

import pytest
from werkzeug.datastructures import FileStorage

from invisible_flow.Storage.IStorage import IStorage
from invisible_flow.Storage.LocalStorage import LocalStorage
from invisible_flow.constants import FOIA_RESPONSE_FIELD_NAME


class TestIStorage:
    subject = IStorage()

    def test_store_throws_exception_when_used(self):
        with pytest.raises(NotImplementedError):
            self.subject.store(None, None)


class TestLocalStorage:
    subject = LocalStorage()
    fake_file_storage = FileStorage(stream=BytesIO(b'Some content'))

    def test_store_does_not_throw_exception_when_used(self):
        self.subject.store('Blah', self.fake_file_storage)
        os.remove('Blah')

    def test_store_writes_file_locally(self):
        self.subject.store(FOIA_RESPONSE_FIELD_NAME, self.fake_file_storage)
        assert os.path.exists(FOIA_RESPONSE_FIELD_NAME)
        os.remove(FOIA_RESPONSE_FIELD_NAME)
