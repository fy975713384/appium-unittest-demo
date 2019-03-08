from handler.guide_handler import GuideHandler


class Guide:

    def __init__(self):
        self._guide = GuideHandler()

    def skip_guide(self):
        self._guide.switch_four()
        self._guide.go_main()