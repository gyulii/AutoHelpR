


from traceback import print_tb


def key_check_if_pressed(key_string, key) -> bool:
    if 'char' in dir(key):
        if key.char == key_string:
            return True
        else:
            return False

def wrapper(func, *args):
    func(*args)


class Task:
    def __init__(self):
        self.task_list = []

    def add_task(self , task):
         self.task_list.append(task)

    def remove_task(self):
        self.task_list.pop()

    def run_task(self):
        for task in self.task_list:
            wrapper(*task)    # * to make the itarable expand in args

    def print_tasks(self):
        for task in self.task_list:
            for element in task:
                if(__name__ in dir(element) ):
                    print(element.__name__)
                else:
                    print(element)








class SubTask(Task):
    pass

def record_mouse_position():
    """Return a 2 element list with current mouse position"""
    pass


def read_clipboard():
    """Returns the content of the clipboard as a string"""
    pass
