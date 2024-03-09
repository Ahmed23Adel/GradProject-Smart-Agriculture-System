from abc import ABC, abstractmethod

class SingleOption(ABC):
    def __init__(self):
        self.msg = ""# must be less than 16 chars
        
    def set_msg(self, msg):
        if len(msg) > 14:
            raise ValueError("Message must be less than 16 characters")
        self.msg =msg
        
    def perform_action(self):
        raise ValueError("Not implemented")
    
    
class SingleOptionInput(ABC):
    def __init__(self):
        self.input = ""
        self.is_mouse_allowed = True
        self.is_keyboard_allowed = True
        
    def append_char(self, c):
        if not self.input == 14:
            self.input += c
        
    def perform_action(self):
        raise ValueError("Not implemented")
    
    
    
class PageOptions(ABC):
    def __init__(self):
        self.options = []
        self.initial_indx = 0
        self.cur_option = None
            
    def show_options(self, display):
        if len(self.options) <=2:
            for indx, option in enumerate(self.options):
                display.lcd_display_string(option.msg, indx+1)
                
    def move_down(self):
        self.options[self.cur_index].set_msg(self.options[self.cur_index].msg[1:])
        self.cur_idx +=1
        self.options[self.cur_index].set_msg("*"+self.options[self.cur_index].msg)
        self.cur_option = self.options[self.cur_index]
        
    def move_up(self):
        self.options[self.cur_index].set_msg(self.options[self.cur_index].msg[1:])
        self.cur_idx -=1
        self.options[self.cur_index].set_msg("*"+self.options[self.cur_index].msg)
        self.cur_option = self.options[self.cur_index]
        
    def perform_action(self):
        self.cur_option.perform_action()
        
                
class GlobalContextLcd():
    def __init__(self,display):
        self.cur_page = None
        self.display = display 
    
    def change_page(self, new_page):
        self.cur_page = new_page
        self.display.lcd_clear()
        self.cur_page.show_options(display)
        
        
        
    def show_page(self):
        self.cur_page.show_options(self.display)
        
    def clear(self):
        self.display.lcd_clear() 
