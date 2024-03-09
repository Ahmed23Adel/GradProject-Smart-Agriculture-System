from OptionAbstract import SingleOption, PageOptions, SingleOptionInput

class EmptyPage(PageOptions):
    def __init__(self, context):
        self.context = context;
        
        
    def show_options(self, display):
        display.lcd_display_string("Empty page", 1)
