from LcdModule.OptionAbstract import SingleOption, PageOptions, SingleOptionInput


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
        if self.input == self.password:
            self.context.change_page()
    
    
class LoginPage(PageOptions):
    
    def __init__(self, context):
        super().__init__(initial_index = 1)
        print("cur_index", self.cur_index)
        self.context = context
        self.options = [LoginHeader(context), LoginInputField(context)]
        self.cur_option = self.options[1]
        self.mark_exist()
        
