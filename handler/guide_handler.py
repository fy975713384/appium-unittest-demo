from page.guide_page import GuidePage


class GuideHandler:
    """ 操作引导页元素
    """

    def __init__(self):
        self.guide_page = GuidePage()

    def switch_two(self):
        self.guide_page.get_button_two().click()

    def switch_three(self):
        self.guide_page.get_button_three().click()

    def switch_four(self):
        self.guide_page.get_button_four().click()

    def go_main(self):
        self.guide_page.get_go_main_button().click()
