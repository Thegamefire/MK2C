#Test file

import mappings
import vgamepad
import time

gamepad = vgamepad.VX360Gamepad()
current_mapping = mappings.mario_kart

def float_to_trigger(number):

    return number * 327.67

while True:
    gamepad.right_joystick(x_value=32767, y_value=0)
    gamepad.press_button(button=vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_B)
    time.sleep(2)
    gamepad.release_button(button=vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_B)
    print("pressed")
    time.sleep(3)
