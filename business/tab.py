from handler.tab_handler import TabBarHandler


class TabBar:
    def __init__(self):
        self._tab = TabBarHandler()

    def switch_user_page(self):
        self._tab.switch_user_page()
