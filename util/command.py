import os
import platform


class Command:
    LIST_ADB_DEVICES = 'adb devices'
    START_APPIUM = 'appium'
    if platform.system().lower() == 'Windows':
        LIST_RUNNING_SERVER = "tasklist | findstr 'node.exe'"
        KILL_PROCESS = "taskkill -F -PID 'node.exe'"
        CHECK_PORT = 'netstat -ano | findstr '
    else:
        LIST_RUNNING_SERVER = "ps -ef | grep 'node' | awk '/appium/{print $2}'"
        KILL_PROCESS = "kill -9 "
        CHECK_PORT = 'lsof -i| grep '

    @classmethod
    def get_cmd_result(cls, com: str) -> list:
        result_list = []
        result = os.popen(com).readlines()
        for i in result:
            if i == '\n':
                continue
            result_list.append(i.strip('\n'))
        return result_list

    @classmethod
    def exec_cmd(cls, com: str):
        os.system(com)
