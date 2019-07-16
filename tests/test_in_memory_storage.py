from io import BytesIO

from werkzeug.datastructures import FileStorage

from invisible_flow.storage.in_memory_storage import InMemoryStorage


class TestInMemoryStorage:
    subject = InMemoryStorage()
    fake_file_storage = FileStorage(stream=BytesIO(b'Some content'))

    def test_store_should_save_files_under_a_path(self):
        self.subject.store('some file name', self.fake_file_storage, 'a/path')

        retrieved_file = self.subject.get('some file name', 'a/path')
        assert retrieved_file == b'Some content'

