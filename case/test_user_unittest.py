import sys
import os

root_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
sys.path.append(root_path)
import unittest
import time
from multiprocessing import Process
from conf.setting import Setting as ST
from util.server import Server
from util.operate_yaml import OperateYAML
from business.guide import Guide
from business.tab import TabBar
from business.user import User
from driver.base_driver import BaseDriver


class TestUser(unittest.TestCase):
    driver = None
    ORDER = None

    @classmethod
    def setUpClass(cls):
        yaml = OperateYAML()
        ST.DEVICENAME = yaml.get_value(f'user_info_{cls.ORDER}', 'deviceName')
        ST.PORT = yaml.get_value(f'user_info_{cls.ORDER}', 'port')
        ST.APP_PATH = f'{root_path}/app/com.codemao.dan_2.0.1_11.apk'
        print(ST.APP_PATH)
        cls.driver = BaseDriver(ST.DEVICENAME, ST.PORT, ST.APP_PATH).driver
        cls.guide = Guide()
        cls.tab = TabBar()
        cls.user = User()

    @classmethod
    def tearDownClass(cls):
        cls.driver.remove_app('com.codemao.dan')
        cls.driver.quit()

    def test_case01(self):
        self.guide.skip_guide()
        self.tab.switch_user_page()
        self.user.open_login_page()
        self.user.login_by_password(username='18339956220', password='qwe123')


def get_case(order):
    TestUser.ORDER = order
    suite = unittest.TestSuite()
    suite.addTest(TestUser('test_case01'))
    unittest.TextTestRunner().run(suite)


if __name__ == "__main__":
    server = Server()
    server.start_appium()
    time.sleep(5)

    for i in range(len(server.device_list)):
        t = Process(target=get_case, args=(i,))
        t.start()
