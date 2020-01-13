import os
import pathlib
from io import BytesIO

from werkzeug.datastructures import FileStorage

from invisible_flow.storage.local_storage import LocalStorage


class TestLocalStorage:
    subject = LocalStorage()
    fake_file_storage = FileStorage(stream=BytesIO(b'Some content'))

    def test_store_byte_string_does_not_throw_exception_when_used(self):
        self.subject.store_byte_string('Blah', b'Some content', '.')
        os.remove(os.path.join(self.subject.local_upload_directory, 'Blah'))

    def test_store_byte_string_writes_file_locally(self):
        self.subject.store_byte_string('test-file.csv', b'Some content', 'subdir')
        assert os.path.exists(os.path.join(self.subject.local_upload_directory, 'subdir', 'test-file.csv'))

        # cleanup
        os.remove(os.path.join(self.subject.local_upload_directory, 'subdir', 'test-file.csv'))
        os.rmdir(os.path.join(self.subject.local_upload_directory, 'subdir'))
        assert not (os.path.exists(os.path.join(self.subject.local_upload_directory, 'subdir', 'test-file.csv')))

    def test_get_retrieves_locally_stored_files(self):
        directory_path = os.path.join(self.subject.local_upload_directory, 'other-subdir')
        pathlib.Path(directory_path).mkdir()

        try:
            with open(os.path.join(directory_path, 'some-file.txt'), 'w') as file:
                file.write('some text')
                file.close()

            assert self.subject.get('some-file.txt', 'other-subdir') == 'some text'
        finally:
            # cleanup
            os.remove(os.path.join(directory_path, 'some-file.txt'))
            os.rmdir(directory_path)
            assert not (os.path.exists(os.path.join(directory_path, 'some-file.txt')))
