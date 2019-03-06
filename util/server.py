from util.dos_cmd import DosCmd
from util.port import Port
from util.operate_yaml import OperateYAML
from multiprocessing import Process


class Server:

    def __init__(self):
        self.dos = DosCmd()
        self.operate_yaml = OperateYAML()
        self.device_list = self._get_devices()

    def _get_devices(self):
        """
        获取设备信息
        """
        devices_list = []
        result_list = self.dos.get_cmd_result('adb devices')
        if len(result_list) >= 2:
            for i in result_list:
                if 'List' in i:
                    continue
                devices_info = i.split('\t')
                if devices_info[1] == 'device':
                    devices_list.append(devices_info[0])
            return devices_list
        else:
            raise Exception('设备未连接')

    def create_port_list(self, start_port):
        """
        创建可用端口
        """
        port = Port()
        port_list = []
        port_list = port.create_port_list(start_port, self.device_list)
        return port_list

    def create_command_ordinal(self, index):
        """
        按次序生成 Appium 服务启动命令
        """
        appium_port_list = self.create_port_list(4700)
        bootstrap_port_list = self.create_port_list(4900)
        device_list = self.device_list
        port = str(appium_port_list[index])
        bp = str(bootstrap_port_list[index])
        device = device_list[index]
        command = f"""appium -p {port} -bp {bp} -U {device} \
        --no-reset --session-override
        """
        self.operate_yaml.write_data(index, port, bp, device)
        return command

    def start_server_ordinal(self, index):
        command = self.create_command_ordinal(index)
        self.dos.excute_cmd(command)

    def stop_server(self, name):
        if name[-4:] != '.exe':
            name += '.exe'
        server_list = self.dos.get_cmd_result(f'tasklist | findstr {name}')
        if len(server_list) > 0:
            self.dos.excute_cmd(f'taskkill -F -PID {name}')

    def start_appium(self):
        """
        功能：根据线程启动 appium 服务
        """
        self.stop_server('node.exe')
        self.operate_yaml.clear_data()

        for i in range(len(self.device_list)):
            appium_start = Process(
                target=self.start_server_ordinal, args=(i,))
            appium_start.start()
