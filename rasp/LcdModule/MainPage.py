from LcdModule.OptionAbstract import SingleOption, PageOptions, SingleOptionInput

class MainStart(SingleOption):
    def __init__(self, context):
        super().__init__()
        self.set_msg("Start round")
        self.context = context
        
    def perform_action(self):
        return None
    
class MainUpload(SingleOption):
    def __init__(self, context):
        super().__init__()
        self.set_msg("Upload")
        self.context = context
        
    def perform_action(self):
        return None
    
    
class MainPage(PageOptions):
    
    def __init__(self, context):
        super().__init__()
        self.context = context
        self.options = [MainStart(context), MainUpload(context)]
        self.cur_option = self.options[0]
        self.mark_exist()
        