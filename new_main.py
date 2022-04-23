import vgamepad as vg
import pynput
import mappings
import controller_buttons
import time

current_mapping=mappings.mario_kart

gamepad = vg.VX360Gamepad()
left_stick_rotation="neutral"
right_stick_rotation="neutral"

direction_dict={
    0:"neutral",
    1:"north",
    2:"northeast",
    3:"east",
    4:"southeast",
    5:"south",
    6:"southwest",
    7:"west",
    8:"northwest",

    "neutral":0,
    "north":1,
    "northeast":2,
    "east":3,
    "southeast":4,
    "south":5,
    "southwest":6,
    "west":7,
    "northwest":8,

    "Up":"north",
    "Right":"east",
    "Down":"south",
    "Left":"west"
}

numpad_equivalents= {
    #pynput.keyboard.Key.insert:"NumPad0",  #Comment because it checks for insert which could screw up other things
    pynput.keyboard.Key.end:"NumPad1",
    pynput.keyboard.Key.down:"NumPad2",
    pynput.keyboard.Key.page_down:"NumPad3",
    pynput.keyboard.Key.left:"NumPad4",
    #pynput.keyboard.<12>:"NumPad5",
    pynput.keyboard.Key.right:"NumPad6",
    pynput.keyboard.Key.home:"NumPad7",
    pynput.keyboard.Key.up:"NumPad8",
    pynput.keyboard.Key.page_up:"NumPad9"
}

def checkStickButtons(stick):
    stick_buttons={}
    for i in current_mapping:
        if current_mapping[i]== stick+"StickUp":
            stick_buttons["north"]=i
        elif current_mapping[i] == stick+"StickLeft":
            stick_buttons["west"] = i
        elif current_mapping[i] == stick+"StickDown":
            stick_buttons["south"] = i
        elif current_mapping[i] == stick+"StickRight":
            stick_buttons["east"] = i
    return stick_buttons

def define_stick_direction(current_direction, added_direction=None, removed_direction=None):
    if added_direction and not removed_direction:
        #direction added
        print("")
        if current_direction == "neutral":  #Neutral
            return added_direction

        elif current_direction == added_direction:      #Shouldn't happen
            print("current_direction == added_direction")

        elif (current_direction=="north" or current_direction=="south") and (added_direction=="west" or added_direction=="east"):   #Two inputs form a diagonal
            return current_direction+added_direction
        elif (current_direction=="west" or current_direction=="east") and (added_direction=="north" or added_direction=="south"):   #Two inputs form a diagonal
            return added_direction+current_direction

        elif abs(direction_dict[current_direction]-direction_dict[added_direction])==4: #Inputs are facing eachother
            return "neutral"

        elif direction_dict[current_direction]%2==0 and not current_direction == "neutral": #Diagonals get an extra input
            if current_direction == "northeast":
                if added_direction == "south":
                    return "east"
                elif added_direction == "west":
                    return "north"
                else:
                    print(f"Impossible (define_stick_direction) added_direction={added_direction}")
            elif current_direction == "southeast":
                if added_direction == "north":
                    return "east"
                elif added_direction == "west":
                    return "south"
                else:
                    print(f"IMpossible (define_stick_direction) added_direction={added_direction}")
            elif current_direction == "southwest":
                if added_direction== "north":
                    return "west"
                elif added_direction == "east":
                    return "south"
                else:
                    print(f"IMPossible (define_stick_direction) added_direction={added_direction}")
            elif current_direction == "northwest":
                if added_direction == "east":
                    return "north"
                elif added_direction == "south":
                    return "west"
                else:
                    print(f"IMPOssible (define_stick_direction) added_direction={added_direction}")
            else:
                print(f"Math mistake (define_stick_direction) current_direction={current_direction}")

    elif removed_direction and not added_direction:
        #removed direction
        if removed_direction == current_direction:
            return "neutral"
        elif removed_direction in current_direction:
            result_direction = current_direction.replace(removed_direction, "")
            return result_direction
        elif not (direction_dict[current_direction]%2==0) or direction_dict[current_direction]==0:
            if direction_dict[removed_direction]<4:
                if direction_dict[direction_dict[removed_direction]+4] == "north" or direction_dict[direction_dict[removed_direction]+4] == "south":
                    return direction_dict[direction_dict[removed_direction]+4]+current_direction
                elif current_direction=="north" or current_direction == "south":
                    return current_direction+direction_dict[direction_dict[removed_direction]+4]
                else:
                    print("Impossible? (define_stick_rotation)")

            else:
                if direction_dict[direction_dict[removed_direction]-4] == "north" or direction_dict[direction_dict[removed_direction]-4] == "south":
                    return direction_dict[direction_dict[removed_direction]-4]+current_direction
                elif current_direction=="north" or current_direction == "south":
                    return current_direction+direction_dict[direction_dict[removed_direction]-4]
                else:
                    print("Impossible? (define_stick_rotation)")
        else:
            print("You didn't think this was possible")
    else: 
        print("define_stick_direction needs either added_direction or removed_direction AND NOT BOTH")

    


def stickmovement(stick, orientation):  #changes the direction of the stick
    global left_stick_rotation
    global right_stick_rotation
    if stick == "left":
        if orientation == "north":
            print(f"the stick is now facing north")
            gamepad.left_joystick_float(x_value_float=0, y_value_float=1)
            left_stick_rotation="north"
        elif orientation == "west":
            print(f"the stick is now facing west")
            gamepad.left_joystick_float(x_value_float=-1, y_value_float=0)
            left_stick_rotation="west"
        elif orientation == "south":
            print("south")
            gamepad.left_joystick_float(x_value_float=0, y_value_float=-1)
            left_stick_rotation="south"
        elif orientation == "east":
            print("east")
            gamepad.left_joystick_float(x_value_float=1, y_value_float=0)
            left_stick_rotation="east"
        #diagonal directions
        elif orientation == "northwest":
            print("northwest")
            gamepad.left_joystick_float(x_value_float=-1, y_value_float=1)
            left_stick_rotation="northwest"
        elif orientation == "southwest":
            print("southwest")
            gamepad.left_joystick_float(x_value_float=-1, y_value_float=-1)
            left_stick_rotation="southwest"
        elif orientation == "southeast":
            print("southeast")
            gamepad.left_joystick_float(x_value_float=1, y_value_float=-1)
            left_stick_rotation="southeast"
        elif orientation == "northeast":
            print("northeast")
            gamepad.left_joystick_float(x_value_float=1, y_value_float=1)
            left_stick_rotation="northeast"
        else:
            print("the stick is now in neutral")
            gamepad.left_joystick_float(x_value_float=0, y_value_float=0)
            left_stick_rotation="neutral"

            #Right Stick

    elif stick == "right":
        if orientation == "north":
            print("north")
            gamepad.right_joystick_float(x_value_float=0, y_value_float=1)
            right_stick_rotation="north"
        elif orientation == "west":
            print("west")
            gamepad.right_joystick_float(x_value_float=-1, y_value_float=0)
            right_stick_rotation="west"
        elif orientation == "south":
            print("south")
            gamepad.right_joystick_float(x_value_float=0, y_value_float=-1)
            right_stick_rotation="south"
        elif orientation == "east":
            print("east")
            gamepad.right_joystick_float(x_value_float=1, y_value_float=0)
            right_stick_rotation="east"
        #diagonal directions
        elif orientation == "northwest":
            print("northwest")
            gamepad.right_joystick_float(x_value_float=-1, y_value_float=1)
            right_stick_rotation="northwest"
        elif orientation == "southwest":
            print("southwest")
            gamepad.right_joystick_float(x_value_float=-1, y_value_float=-1)
            right_stick_rotation="southwest"
        elif orientation == "southeast":
            print("southeast")
            gamepad.right_joystick_float(x_value_float=1, y_value_float=-1)
            right_stick_rotation="southeast"
        elif orientation == "northeast":
            print("northeast")
            gamepad.right_joystick_float(x_value_float=1, y_value_float=1)
            right_stick_rotation="northeast"
    gamepad.update()

def pressed_dict():
    pressed_dict={
        "²":False,
        pynput.keyboard.Key.insert:False
    }
    for item in current_mapping:
        pressed_dict[item]=False
    return pressed_dict

def get_mapped_button(key):
    key_value=current_mapping[key]
    if key_value in controller_buttons.xbox:
        return controller_buttons.xbox[key_value]
    else:
        print("The button this key is mapped to doesn't exist, please check mappings.py")

###########################################
#### What happens when a key is pressed ###
###########################################

def key_to_buttonpress(key):
    if key in current_mapping:
        if not pressed_dict[key]:

            #StickMovement
            if current_mapping[key].startswith("LeftStick") or current_mapping[key].startswith("RightStick"):
                if current_mapping[key].startswith("LeftStick"):
                    new_direction = direction_dict[current_mapping[key][9:]]
                    print(f"new_direction = {new_direction}")
                    rotation_goal = define_stick_direction(left_stick_rotation, added_direction=new_direction)
                    stickmovement("left", rotation_goal)
                else:
                    new_direction = direction_dict[current_mapping[key][10:]]
                    rotation_goal = define_stick_direction(right_stick_rotation, added_direction=new_direction)
                    stickmovement("right", rotation_goal)

            elif current_mapping[key]=="LT" or current_mapping[key]=="RT":  #Triggers
                if current_mapping[key] == "LT":
                    gamepad.left_trigger_float(1)
                else: 
                    gamepad.right_trigger_float(1)

            else:       #ButtonPress
                print(current_mapping[key])
                button_to_press=get_mapped_button(key)
                if button_to_press:
                    gamepad.press_button(button=button_to_press)
                    gamepad.update()
            pressed_dict[key]=True

def on_keyboard_press(key):
    global two_pressed
    if key in numpad_equivalents and pressed_dict[pynput.keyboard.Key.insert]:
        key=numpad_equivalents[key]
        key_to_buttonpress(pynput.keyboard.Key.shift)
        print(key)
    if hasattr(key, 'vk'):
        if 96<=key.vk <=105:
            key="NumPad"+str(key.vk-96)
        elif key.vk == 12:
            key = "NumPad5"
            key_to_buttonpress(pynput.keyboard.Key.shift)
    if hasattr(key, 'char'):
        key=key.char
        if hasattr(key, 'lower'):
            key=key.lower()
        if key =='²' and not pressed_dict[key]:
            pressed_dict[key]=True
    key_to_buttonpress(key)
    if key == pynput.keyboard.Key.insert and not pressed_dict[key]:
        pressed_dict[key]=True

    if key == pynput.keyboard.Key.esc and pressed_dict['²']:
        global time_to_stop
        time_to_stop=True

def key_to_buttonrelease(key):
    if key in current_mapping:
        if current_mapping[key].startswith("LeftStick") or current_mapping[key].startswith("RightStick"):
            if current_mapping[key].startswith("LeftStick"):
                new_direction=direction_dict[current_mapping[key][9:]]
                rotation_goal = define_stick_direction(left_stick_rotation, removed_direction=new_direction)
                stickmovement("left", rotation_goal)
            else:
                new_direction=direction_dict[current_mapping[key][10:]]
                rotation_goal = define_stick_direction(right_stick_rotation, removed_direction=new_direction)
                stickmovement("right", rotation_goal)
        elif current_mapping[key]=="LT" or current_mapping[key]=="RT":  #Triggers
                if current_mapping[key] == "LT":
                    gamepad.left_trigger_float(0)
                else: 
                    gamepad.right_trigger_float(0)
        else:
            button_to_release=get_mapped_button(key)
            if button_to_release:
                gamepad.release_button(button=button_to_release)
                gamepad.update()
        pressed_dict[key]=False

def on_keyboard_release(key):
    global two_pressed
    if key in numpad_equivalents and pressed_dict[pynput.keyboard.Key.insert]:
        key=numpad_equivalents[key]
    if hasattr(key, 'vk'):
        if 96<=key.vk <=105:
            key="NumPad"+str(key.vk-96)
    if hasattr(key, 'char'):
        key=key.char
        if hasattr(key, 'lower'):
            key=key.lower()
        if key =='²':
            pressed_dict[key]=True
    key_to_buttonrelease(key)
    if key == pynput.keyboard.Key.insert:
        pressed_dict[key]=False

def start():
    global pressed_dict
    pressed_dict=pressed_dict()
    global left_stick_buttons
    global right_stick_buttons
    left_stick_buttons = checkStickButtons('left')
    right_stick_buttons = checkStickButtons('right')
    keyboard_listener=pynput.keyboard.Listener(on_press=on_keyboard_press, on_release=on_keyboard_release)
    keyboard_listener.start()
    global time_to_stop
    time_to_stop=False
    while not time_to_stop:
        time.sleep(1)
    keyboard_listener.stop()


start()
