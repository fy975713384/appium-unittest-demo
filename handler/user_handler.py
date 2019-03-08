from page.user_page import UserPage, LoginPage, RegPage


class UserPageHandler:

    def __init__(self):
        self.user_page = UserPage()

    def touch_user_head(self):
        self.user_page.get_user_head().click()


class LoginPageHandler:

    def __init__(self):
        self.login_page = LoginPage()

    def input_username(self, username: str):
        self.login_page.get_username_textbox().send_keys(username)

    def input_password(self, password: str):
        self.login_page.get_password_textbox().send_keys(password)

    def touch_login_button(self):
        self.login_page.get_login_button().click()


class RegPageHandler:

    def __init__(self):
        self.reg_page = RegPage()
