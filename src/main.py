from pynput import keyboard
import pyautogui
from src.task import record_mouse_position

import task as ts


Task1 = ts.Task()


p
record_task = True

Task1.add_task([pyautogui.click, *pyautogui.position()]) 
Task1.print_tasks()

def on_press(key):


    if key == keyboard.Key.esc:
        listener_basic_key.stop()

    if(record_task == True):
        if (ts.key_check_if_pressed('r', key)):
            print("Clicking task added")
            Task1.add_task([pyautogui.click, *pyautogui.position()]) 
        if (ts.key_check_if_pressed('d', key)):
            print("Last Task removed")
            Task1.remove_task()
        if (ts.key_check_if_pressed('p', key)):
            print("Last Task removed")
            Task1.print_tasks()
        

def on_release(key):
    pass


def ctrl_y():
    print('<ctrl>+y = Task adding mode')
    record_task = True
    

def ctrl_d():
    print('<ctrl>+d = Running tasks')
    Task1.run_task()



listener_basic_key =  keyboard.Listener(on_press=on_press, on_release=on_release)

listener_special_keys =  keyboard.GlobalHotKeys({
        '<ctrl>+y': ctrl_y,
        '<ctrl>+d': ctrl_d
        })


listener_basic_key.start()
listener_special_keys.start()

listener_basic_key.join()