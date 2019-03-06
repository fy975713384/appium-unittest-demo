from util.element import Element


class PolicyPopup:
    # 获取隐私政策弹窗元素信息
    def __init__(self):
        self.element = Element('policy')

    def get_title_element(self):
        return self.element.get_element('title')

    def get_policy_link(self):
        return self.element.get_element('pol_link')

    def get_ignore_button(self):
        return self.element.get_element('ignore')

    def get_accept_button(self):
        return self.element.get_element('accept')
