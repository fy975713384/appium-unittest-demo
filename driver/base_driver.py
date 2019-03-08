from appium import webdriver
from util.singleton import singleton


@singleton
class BaseDriver:

    def __init__(self, devicename, port, app_path):
        self.deviceName = devicename
        self.port = port
        self.app_path = app_path
        self.driver = self._get_driver()

    def _android_driver(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": self.deviceName,
            "app": self.app_path,
            "autoGrantPermissions": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True
        }

        driver = webdriver.Remote(
            f'http://localhost:{self.port}/wd/hub', desired_caps)
        driver.implicitly_wait(10)
        return driver

    def _ios_driver(self):
        pass

    def _get_driver(self):
        return self._android_driver()
