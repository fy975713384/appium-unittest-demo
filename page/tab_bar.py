from util.element import Element


class TabBar:
    # 获取底部导航栏元素信息
    def __init__(self):
        self.element = Element('tab')

    def get_home_button(self):
        return self.element.get_element('home')

    def get_watermelon_button(self):
        return self.element.get_element('watermelon')

    def get_send_button(self):
        return self.element.get_element('send')

    def get_volcano_button(self):
        return self.element.get_element('volcano')

    def get_user_button(self):
        return self.element.get_element('user_info')
