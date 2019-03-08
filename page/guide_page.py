from util.element import Element


class GuidePage:
    """ 获取引导页元素信息
    """

    def __init__(self):
        self.element = Element('guide')

    def get_button_one(self):
        return self.element.get_element('page_one')

    def get_button_two(self):
        return self.element.get_element('page_two')

    def get_button_three(self):
        return self.element.get_element('page_three')

    def get_button_four(self):
        return self.element.get_element('page_four')

    def get_go_main_button(self):
        return self.element.get_element('go_main')
