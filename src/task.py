def record_mouse_position():
    """Return a 2 element list with current mouse position"""
    pass


def read_clipboard():
    """Returns the content of the clipboard as a string"""
    pass



class KeyCombination:
    def __init__(self , combination):
        self.combination = combination
        self.current_state = set()
        pass
    def key_combination_pressed(self, key):
        if key in self.combination:
            self.current_state.add(key)
            if all(key in self.current_state for key in self.combination):
                return True
            else:
                return False
    def key_combination_released(self, key):
        self.current_state.remove(key)


def key_check_if_pressed(key_string , key):
    if 'char' in dir(key):
     if key.char == key_string:
        return True
    else:
        return False


class SubTask:
    """Have an action to execute """
    """Have a name, functions"""
    pass
