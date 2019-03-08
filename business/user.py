from handler.user_handler import UserPageHandler
from handler.user_handler import LoginPageHandler
from handler.user_handler import RegPageHandler


class User:
    def __init__(self):
        self._user = UserPageHandler()
        self._login = LoginPageHandler()
        self._register = RegPageHandler()

    def open_login_page(self):
        self._user.touch_user_head()

    def login_by_password(self, username: str, password: str):
        self._login.input_username(username)
        self._login.input_password(password)
        self._login.touch_login_button()
