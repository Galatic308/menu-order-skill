from mycroft import MycroftSkill, intent_file_handler


class MenuOrder(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('order.menu.intent')
    def handle_order_menu(self, message):
        self.speak_dialog('order.menu')
        
    @intent_file_handler('order.menu.intent')
    def order_food(self, message):
        self.speak_dialog('welcome to cyber food may i take your order')
        
    def order_food(self, message):
    if message > order_food:
        self.message_intent('i would like a burger')
        self.speak_dialog('one burger coming right up')
    
    if message > order_food:
        self.message_intent('i would like a chicken sandwich')
        self.speak_dialog('one chicken sandwich coming right up')
        
     if message < order_food:
         self.message_intent('i would like pizza')
         self.speak_dialog('im sorry we dont have pizza on the menu')
        
    @intent_file_handler('order.menu.intent')
    def order_side(self, message):
        self.speak_dialog('what would you like for a side')
        
     def order_side(self, message):
        if message > order_side:
         self.message_intent('i would like some french fries')
         self.speak_dialog('french fires coming right')
        if message < order_side:
        self.message_intent('i would like some onion rings')
        self.speak_dialog('im sorry we dont have onion rings on the menu')
        
    @intent_file_handler('order.menu.intent')
    def order_drink(self, message):
        self.speak_dialog('what would you like to drink')
        
    @intent_file_handler('order.menu.intent')
    def order_drink(self, message):
    
        if message > order_drink:
        self.message_intent('i would like a coke')
        self.speak_dialog('one coke coming right up')
        
        if message > order_drink:
        self.message_intent('i would like a orange drink')
        self.speak_dialog('one orange drink coming right up')
        
        if message > order_drink:
        self.message_intent('i would like a sprite')
        self.speak_dialog('one sprite coming right up')
        
        if message < order_drink:
        self.message_intent('i would like a pepsi')
        self.speak_dialog('im sorry we only have coke products')
        
        if message < order_drink:
        self.message_intent('i would like a mountain dew')
        self.speak_dialog('im sorry we only have coke products')
        
    @intent_file_handler('order.menu.intent')
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

