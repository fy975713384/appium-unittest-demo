from page.tab_bar import TabBar


class TabBarHandler:

    def __init__(self):
        self.tab_bar = TabBar()

    def switch_home_page(self):
        self.tab_bar.get_home_button().click()

    def switch_watermelon_page(self):
        self.tab_bar.get_watermelon_button().click()

    def switch_send_page(self):
        self.tab_bar.get_send_button().click()

    def switch_volcano(self):
        self.tab_bar.get_volcano_button().click()

    def switch_user_page(self):
        self.tab_bar.get_user_button().click()
