from configparser import ConfigParser
import os


class ReadConf:
    """docstring for ReadConf"""

    def __init__(self):
        self.file_path = os.path.split(os.path.dirname(__file__))[
            0] + '\\conf\\LocalElement.ini'
        # print(self.file_path)
        self.data = self._read_conf()

    def _read_conf(self):
        read_conf = ConfigParser()
        read_conf.read(self.file_path)
        return read_conf

    def get_value(self, sec, key):
        return self.data.get(sec, key)
