from LcdModule.OptionAbstract import SingleOption, PageOptions
from LcdModule.Login import LoginPage

class HelloOption(SingleOption):
    def __init__(self, context):
        self.set_msg("Hi Rowling")
        self.context = context
        
    def perform_action(self):
        self.context.change_page(LoginPage(self.context))
        
        
class HelloPlantMagic(SingleOption):
    def __init__(self, context):
        self.set_msg("Plants Magic")
        self.context = context
        
    def perform_action(self):
        self.context.chage_page(LoginPage(self.context))
        
class HelloWebsite(SingleOption):
    def __init__(self, context):
        self.set_msg("Rowling.com")
        self.context = context
        
    def perform_action(self):
        self.context.chage_page(LoginPage(self.context))
        
        
class HelloPage(PageOptions):
    def __init__(self,context):
        super().__init__()
        self.context = context
        self.options = [HelloOption(self.context), HelloPlantMagic(self.context), HelloWebsite(self.context)]
        self.cur_option = self.options[0]
        self.mark_exist()
        
        
        
        
