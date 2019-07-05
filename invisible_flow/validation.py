
valid_extensions = ('.xls', '.csv', '.xlsx')


def is_valid_file_type(filename):
    return filename != '' and filename.endswith(valid_extensions)
