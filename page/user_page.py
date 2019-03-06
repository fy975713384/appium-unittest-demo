from util.element import Element


class UserPage:
    # 获取用户页面元素信息
    def __init__(self):
        self.element = Element('user')

    def get_login_button(self):
        return self.element.get_element('login')

    def get_my_cllection_button(self):
        return self.element.get_element('my_cllection')

    def get_my_comment_button(self):
        pass

    def get_my_favour_button(self):
        pass

    def get_browse_his_button(self):
        pass


class LoginPage:
    # 获取登录页面元素信息
    def __init__(self):
        self.element = Element('login')

    def get_title_element(self):
        return self.element.get_element('title')

    def get_login_by_pw_button(self):
        return self.element.get_element('login_by_pw')

    def get_phone_number_textbox(self):
        return self.element.get_element('phone_number')

    def get_password_textbox(self):
        return self.element.get_element('password')

    def get_login_button(self):
        return self.element.get_element('login_button')


class RegistPage:
    # 获取注册页面元素信息
    def __init__(self):
        self.element = Element('signup')

    def get_login_button(self):
        return self.element.get_element('login_immed')
