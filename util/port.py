from util.command import Command


class Port:
    """
    封装对端口进行操作的函数
    """

    @classmethod
    def port_is_used(cls, port_num):
        """
        判断端口是否被占用
        :param port_num:
        :return:
        """
        _cmd = Command()
        command = f'{Command.CHECK_PORT}{str(port_num)}'
        result = _cmd.get_cmd_result(command)
        if len(result) > 0:
            flag = True
        else:
            flag = False
        return flag

    @classmethod
    def create_port_list(cls, start_port, device_list) -> list:
        """
        生成可用端口列表
        @parameter start_port
        @parameter device_list
        """
        port_list = []
        if device_list is not None:
            while len(port_list) != len(device_list):
                if cls.port_is_used(start_port) is not True:
                    port_list.append(start_port)
                start_port = start_port + 1
            return port_list
        else:
            print('生成可用端口失败！')
            return []
