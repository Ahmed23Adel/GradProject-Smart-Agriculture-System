from LcdModule.OptionAbstract import SingleOption, PageOptions, SingleOptionInput
#from LcdModule.EmptyModule import SingleOption, PageOptions, SingleOptionInput
from LcdModule.MainPage import MainPage


class LoginHeader(SingleOption):
    def __init__(self, context):
        super().__init__()
        self.set_msg("Password:")
        self.context = context
        
    def perform_action(self):
        return None
        
class LoginInputField(SingleOptionInput):
    def __init__(self, context):
        super().__init__()
        self.context = context
        self.username = "rowling"
        self.password = "1234"
        
    def perform_action(self):
        if self.msg[1:] == self.password:
            print("log")
            self.context.change_page(MainPage(self.context))
        print("not log")
    
class LoginPage(PageOptions):
    
    def __init__(self, context):
        super().__init__(initial_index = 1)
        print("cur_index", self.cur_index)
        self.context = context
        self.options = [LoginHeader(context), LoginInputField(context)]
        self.cur_option = self.options[1]
        self.mark_exist()
        
