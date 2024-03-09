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
    
    def append_char(self, c):
        return False
    
    
class SingleOptionInput(ABC):
    def __init__(self):
        self.msg = ""
        self.is_mouse_allowed = True
        self.is_keyboard_allowed = True
        self.last_char="D"
        
    def append_char(self, c):
        print("char: ",c)
        if c == self.last_char:
            self.perform_action()
            return False
        if not len(self.msg) == 14:
            self.msg += c
        return True
        
    def perform_action(self):
        raise ValueError("Not implemented")
    
    def set_msg(self, msg):
        if len(msg) > 14:
            raise ValueError("Message must be less than 16 characters")
        self.msg =msg
    
class PageOptions(ABC):
    def __init__(self, initial_index = 0):
        self.options = []
        self.intial_index = initial_index
        self.cur_option = None
        self.cur_index = self.intial_index
        
        
    def mark_not_exist(self):
        self.options[self.cur_index].set_msg(self.options[self.cur_index].msg[1:])
        
    def mark_exist(self):
        self.options[self.cur_index].set_msg("*"+self.options[self.cur_index].msg)
        self.cur_option = self.options[self.cur_index]
            
    def show_options(self, display):
        if self.cur_index == len(self.options)-1:
            print("in last", self.cur_index, len(self.options)-1)
            display.lcd_display_string(self.options[self.cur_index-1].msg, 1)
            display.lcd_display_string(self.options[self.cur_index].msg, 2)
        else:
            display.lcd_display_string(self.options[self.cur_index].msg, 1)
            display.lcd_display_string(self.options[self.cur_index+1].msg, 2)
                
                    
                
    def move_down(self):
        if self.cur_index == len(self.options)-1:
            return
        print("Moving down in page")
        self.mark_not_exist()
        self.cur_index +=1
        self.mark_exist()
        self.cur_option = self.options[self.cur_index]
        print([x.msg for x in self.options])
        
    def move_up(self):
        self.mark_not_exist()
        self.cur_index -=1
        self.mark_exist()
        self.cur_option = self.options[self.cur_index]
        
    def perform_action(self):
        self.cur_option.perform_action()
        
    def append_char(self, c):
        return self.options[self.cur_index].append_char(c)
 
                
class GlobalContextLcd():
    def __init__(self,display):
        self.cur_page = None
        self.display = display 
    
    def change_page(self, new_page):
        self.cur_page = new_page
        self.display.lcd_clear()
        self.cur_page.show_options(self.display)
        
        
        
    def show_page(self):
        self.cur_page.show_options(self.display)
  
    def move_up(self):
        self.cur_page.move_up()
        self.refresh()
        
    def move_down(self):
        self.cur_page.move_down()
        self.refresh()
       
    def perform_action(self):
        self.cur_page.perform_action()
       
    def refresh(self):
        self.clear()
        self.show_page()
        
    def clear(self):
        self.display.lcd_clear()
        
    def append_char(self, c):
        if self.cur_page.append_char(c):
            self.refresh()
