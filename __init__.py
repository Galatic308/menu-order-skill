from mycroft import MycroftSkill, intent_file_handler


class MenuOrder(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('order.menu.intent')
    def handle_order_menu(self, message):
        self.speak_dialog('order.menu')


def create_skill():
    return MenuOrder()

