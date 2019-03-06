import sys
import os
root_path = os.path.split(os.path.dirname(__file__))[0]
sys.path.append(root_path)
import unittest
import time
from multiprocessing import Process
from conf.setting import Setting as ST
from util.server import Server
from util.operate_yaml import OperateYAML
from handler.policy_handler import PolicyPopupHandler
from handler.tab_handler import TabBarHandler
from handler.user_handler import UserPageHandler, LoginPageHandler


class Testup(unittest.TestCase):

    ORDER = None

    @classmethod
    def setUpClass(cls):
        yaml = OperateYAML()
        ST.DEVICENAME = yaml.get_value(f'user_info_{cls.ORDER}', 'deviceName')
        ST.PORT = yaml.get_value(f'user_info_{cls.ORDER}', 'port')
        ST.APP_PATH = f'{root_path}\\app\\jrtt.apk'
        cls.policy = PolicyPopupHandler()
        cls.tab = TabBarHandler()
        cls.user = UserPageHandler()
        cls.login = LoginPageHandler()

    def test_case01(self):
        '''
        验证首次登录时，打开注册页面
        '''
        self.policy.accept_policy()
        self.tab.switch_user_page()
        self.user.touch_login_button()
        assert self.login.get_title_text() == '账号注册'

    @classmethod
    def tearDownClass(cls):
        pass


def get_case(order):
    Testup.ORDER = order
    suite = unittest.TestSuite()
    suite.addTest(Testup('test_case01'))
    unittest.TextTestRunner().run(suite)


if __name__ == "__main__":
    server = Server()
    server.start_appium()
    time.sleep(5)

    for i in range(len(server.device_list)):
        t = Process(target=get_case, args=(i,))
        t.start()
