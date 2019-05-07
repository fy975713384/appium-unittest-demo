import yaml
import os
from util.singleton import singleton


@singleton
class HandleDriverConf:

    def __init__(self, file_path=None):
        if file_path is None:
            self.yaml_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0] + '/conf/DriverConf.yml'
        else:
            self.yaml_path = file_path

    def read_data(self):
        with open(self.yaml_path) as f:
            data = yaml.load(f)
        return data

    def get_value(self, k1, k2):
        data = self.read_data()
        value = data[k1][k2]
        return value

    def write_data(self, index, port, bp, device):
        data = self._join_data(index, port, bp, device)
        with open(self.yaml_path, 'a') as f:
            yaml.dump(data, f)

    def _join_data(self, index, port, bp, device):
        data = {
            'user_info_' + str(index): {
                'port': port,
                'bp': bp,
                'deviceName': device,
            }
        }
        return data

    def clear_data(self):
        with open(self.yaml_path, 'w') as f:
            f.truncate()
