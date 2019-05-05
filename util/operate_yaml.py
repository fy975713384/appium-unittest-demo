import yaml
import os


class OperateYAML:

    def __init__(self):
        self.yaml_path = os.path.split(os.path.dirname(__file__))[
            0] + '/conf/DriverConf.yml'

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
