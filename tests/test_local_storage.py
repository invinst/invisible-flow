import os
import pathlib
from io import BytesIO

from werkzeug.datastructures import FileStorage

from invisible_flow.storage.local_storage import LocalStorage


class TestLocalStorage:
    subject = LocalStorage()
    fake_file_storage = FileStorage(stream=BytesIO(b'Some content'))

    def test_store_does_not_throw_exception_when_used(self):
        self.subject.store('Blah', self.fake_file_storage, '.')
        os.remove(os.path.join('local_upload', 'Blah'))

    def test_store_writes_file_locally(self):
        self.subject.store('test-file.csv', self.fake_file_storage, 'subdir')
        assert os.path.exists(os.path.join('local_upload', 'subdir', 'test-file.csv'))

        # cleanup
        os.remove(os.path.join('local_upload', 'subdir', 'test-file.csv'))
        os.rmdir(os.path.join('local_upload', 'subdir'))
        assert not (os.path.exists(os.path.join('local_upload', 'subdir', 'test-file.csv')))

    def test_get_retrieves_locally_stored_files(self):
        pathlib.Path('other-subdir').mkdir()
        with open(os.path.join('other-subdir', 'some-file.txt'), 'w') as file:
            file.write('some text')
            file.close()

        assert self.subject.get('some-file.txt', 'other-subdir') == 'some text'

        # cleanup
        os.remove(os.path.join('other-subdir', 'some-file.txt'))
        os.rmdir('other-subdir')
        assert not (os.path.exists(os.path.join('other-subdir', 'some-file.txt')))
