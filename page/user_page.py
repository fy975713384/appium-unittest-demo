from util.element import Element


class UserPage:
    """ 获取用户页面元素信息
    """

    def __init__(self):
        self.element = Element('user')

    def get_user_head(self):
        return self.element.get_element('user_head')

    def get_my_collect_button(self):
        return self.element.get_element('my_collect')

    def get_setting_button(self):
        return self.element.get_element('setting')

    def get_about_button(self):
        return self.element.get_element('about')


class LoginPage:
    """ 获取登录页面元素信息
    """

    def __init__(self):
        self.element = Element('login')

    def get_username_textbox(self):
        return self.element.get_element('username')

    def get_password_textbox(self):
        return self.element.get_element('password')

    def get_login_button(self):
        return self.element.get_element('login_bt')

    def get_find_password_button(self):
        return self.element.get_element('find_pw')

    def get_clean_username_button(self):
        return self.element.get_element('un_clean')

    def get_login_by_qq_button(self):
        pass

    def get_login_by_wc_button(self):
        pass


class RegPage:
    """ 获取注册页面元素信息
    """

    def __init__(self):
        self.element = Element('signup')
