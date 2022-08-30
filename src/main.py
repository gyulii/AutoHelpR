
from pynput import keyboard
import task as ts


comb_alt_ctrl = ts.KeyCombination({keyboard.Key.alt_l, keyboard.Key.ctrl_l})

def on_press(key):
    if(comb_alt_ctrl.key_combination_pressed(key)):
        print('All modifiers active!')

    if key == keyboard.Key.esc:
        listener.stop()

    if(ts.key_check_if_pressed('a' , key)):
            print("QQQQQQQ")


def on_release(key):
    comb_alt_ctrl.key_combination_released(key)



with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
