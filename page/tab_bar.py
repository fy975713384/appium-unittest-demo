from util.element import Element


class TabBar:
    # 获取底部导航栏元素信息
    def __init__(self):
        self.element = Element('tab')

    def get_discover_button(self):
        return self.element.get_element('discover')

    def get_class_button(self):
        return self.element.get_element('pub_class')

    def get_community_button(self):
        return self.element.get_element('community')

    def get_user_button(self):
        return self.element.get_element('user_info')
