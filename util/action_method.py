class ActionMethod:

    def __init__(self, driver):
        self.driver = driver

    # 获取屏幕尺寸
    def get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    # 向上滑动
    def swipe_up(self):
        x = self.get_size()[0] / 2
        y0 = self.get_size()[1] / 10 * 6
        y1 = self.get_size()[1] / 10 * 4
        self.driver.swipe(x, y0, x, y1)

    # 向下滑动
    def swipe_down(self):
        x = self.get_size()[0] / 2
        y0 = self.get_size()[1] / 10 * 4
        y1 = self.get_size()[1] / 10 * 6
        self.driver.swipe(x, y0, x, y1)

    # 向右滑动
    def swipe_right(self):
        y = self.get_size()[0] / 2
        x0 = self.get_size()[1] / 4 * 1
        x1 = self.get_size()[1] / 4 * 3
        self.driver.swipe(x0, y, x1, y)

    # 向左滑动
    def swipe_left(self):
        y = self.get_size()[0] / 2
        x0 = self.get_size()[1] / 4 * 3
        x1 = self.get_size()[1] / 4 * 1
        self.driver.swipe(x0, y, x1, y)
