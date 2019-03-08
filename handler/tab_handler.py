from page.tab_bar import TabBar


class TabBarHandler:

    def __init__(self):
        self.tab_bar = TabBar()

    def switch_discover_page(self):
        self.tab_bar.get_discover_button().click()

    def switch_pub_class_page(self):
        self.tab_bar.get_class_button().click()

    def switch_community_page(self):
        self.tab_bar.get_community_button().click()

    def switch_user_page(self):
        self.tab_bar.get_user_button().click()
