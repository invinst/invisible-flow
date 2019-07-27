import os


class IFTestBase:
    package_directory = os.path.dirname(os.path.abspath(__file__))
    resource_directory = os.path.join(package_directory, 'resources')
