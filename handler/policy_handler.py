from page.policy_popup import PolicyPopup


class PolicyPopupHandler:

    def __init__(self):
        self.policy_popup = PolicyPopup()

    def accept_policy(self):
        self.policy_popup.get_accept_button().click()
