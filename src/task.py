
class KeyCombination:
    """Class for managing pressed keyboard combination by updating an internal

    Input: from pynput:keyboard.Key

    On press event call: key_combination_pressed(key)

    On release event call: key_combination_released(key)
    """

    def __init__(self, combination):
        self.key_combination = combination
        self.current_key_states_list = set()
        pass

    def key_combination_pressed(self, key) -> bool:
        """Adds the currently pressed key to the class set and returns True if all key is in the list."""
        if key in self.key_combination:
            self.current_key_states_list.add(key)
            if all((key in self.current_key_states_list) for key in self.key_combination):
                return True
            else:
                return False

    def key_combination_released(self, key):
        if (key in self.current_key_states_list):
            self.current_key_states_list.remove(key)


def key_check_if_pressed(key_string, key) -> bool:
    if 'char' in dir(key):
        if key.char == key_string:
            return True
        else:
            return False


class Task:
    """Have an action to execute """
    """Have a name, functions"""
    pass


class SubTask(Task):
    pass

def record_mouse_position():
    """Return a 2 element list with current mouse position"""
    pass


def read_clipboard():
    """Returns the content of the clipboard as a string"""
    pass
