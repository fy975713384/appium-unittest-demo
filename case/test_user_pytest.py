# import os
# import pytest
# from util.operate_yaml import OperateYAML
# from conf.setting import Setting as ST
# from util.server import Server
# from business.guide import Guide
# from driver.base_driver import BaseDriver
# from multiprocessing import Process
#
# global ORDER
#
#
# class TestUserPage:
#
#     @pytest.fixture(scope='class')
#     def driver_option(self):
#         ym = OperateYAML()
#         ST.DEVICENAME = ym.get_value(f'user_info_{ORDER}', 'deviceName')
#         ST.PORT = ym.get_value(f'user_info_{ORDER}', 'port')
#         root_path = os.path.split(os.path.dirname(__file__))[0]
#         ST.APP_PATH = f'{root_path}\\app\\com.codemao.dan_2.0.1_11.apk'
#
#     @pytest.fixture(scope='function')
#     def app_option(self, driver_option):
#         guide = Guide()
#         guide.skip_guide()
#         yield
#         BaseDriver(ST.DEVICENAME, ST.PORT, ST.APP_PATH).driver.close_app()
#
#     def test_demo01(self, app_option):
#         pass
#
#
# if __name__ == '__main__':
#     server = Server()
#     server.start_appium()
#     yaml = OperateYAML()
#     for ORDER in range(len(server.device_list)):
#         t = Process(target=pytest.main())
#         t.start()
