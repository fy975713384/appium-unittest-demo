from page.user_page import UserPage, LoginPage, RegistPage


class UserPageHandler:

    def __init__(self):
        self.user_page = UserPage()

    def touch_login_button(self):
        # 点击用户信息界面的登录图标按钮
        self.user_page.get_login_button().click()


class LoginPageHandler:

    def __init__(self):
        self.login_page = LoginPage()

    def get_title_text(self):
        self.login_page.get_title_element().text

    def switch_login_by_password(self):
        self.login_page.get_login_by_pw_button().click()

    def input_phone_number(self):
        self.login_page.get_phone_number_textbox().send_keys('17607550667')

    def input_password(self):
        self.login_page.get_password_textbox().send_keys('@pf1.01.00.1')

    def login(self):
        self.login_page.get_login_by_pw_button().click()


class RegistPageHandler:

    def __init__(self):
        self.regist_page = RegistPage()

    def login_immediate(self):
        self.regist_page.get_login_button().click()
