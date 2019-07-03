import os

valid_extensions = ['.xls', '.csv', '.xlsx']


def are_valid_file_extensions(filename):
    (file_name, file_extension) = os.path.splitext(filename)
    return file_extension in valid_extensions

