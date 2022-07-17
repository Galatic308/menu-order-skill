from mycroft import MycroftSkill, intent_file_handler


class MenuOrder(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('order.menu.intent')
    def handle_order_menu(self, message):
        self.speak_dialog('order.menu')
    def order_food(self, message):
        self.message_intent('i would like a burger')
        self.speak_dialog('one burger coming right up')
        
    def order_food(self, message):
        self.message_intent('i would like a chicken sandwich')
        self.speak_dialog('one chicken sandwich coming right up')
        
     def order_food(self, message):
         self.message_intent('i would like a pizza sandwich')
         self.speak_dialog('im sorry we dont have pizza on the menu')
         
    def order_side(self, message):
        self.speak_dialog('what would you like for a side')
        
     def order_side(self, message):
         self.message_intent('i would like some french fries')
         self.speak_dialog('french fires coming right')
         
    def order_side(self, message):
        self.message_intent('i would like some onion rings')
        self.speak_dialog('im sorry we dont have onion rings on the menu')
        
    def order_drink(self, message):
        self.speak_dialog('what would you like to drink')
        
    def order_drink(self, message):
        self.message_intent('i would like a coke')
        self.speak_dialog('one coke coming right up')
        
    def order_drink(self, message):
        self.message_intent('i would like a orange drink')
        self.speak_dialog('one orange drink coming right up')
        
    def order_drink(self, message):
        self.message_intent('i would like a sprite')
        self.speak_dialog('one sprite coming right up')
        
    def order_drink(self, message):
        self.message_intent('i would like a pepsi')
        self.speak_dialog('im sorry we only have coke products')
        
    def order_drink(self, message):
        self.message_intent('i would like a mountain dew')
        self.speak_dialog('im sorry we only have coke products')
        
    def confirm_your_order(self, message):
        self.message_intent('i would like to confirm my order')
        self.speak_dialog('would you like to confirm your order')
        if(no>yes):
            self.message_intent('no')
            self.speak_dialog('alright take your time')
        if(no<yes):
            self.message_intent('yes')
            self.speak_dialog('your order has been confirmed enjoy your meal')

def create_skill():
    return MenuOrder()

