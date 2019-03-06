# 获取屏幕尺寸
def get_size():
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width, height


# 向上滑动
def swipe_up():
    x = get_size()[0] / 2
    y0 = get_size()[1] / 10 * 6
    y1 = get_size()[1] / 10 * 4
    driver.swipe(x, y0, x, y1)


# 向下滑动
def swipe_down():
    x = get_size()[0] / 2
    y0 = get_size()[1] / 10 * 4
    y1 = get_size()[1] / 10 * 6
    driver.swipe(x, y0, x, y1)


# 向右滑动
def swipe_right():
    y = get_size()[0] / 2
    x0 = get_size()[1] / 4 * 1
    x1 = get_size()[1] / 4 * 3
    driver.swipe(x0, y, x1, y)


# 向左滑动
def swipe_left():
    y = get_size()[0] / 2