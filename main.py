#Beste toekomst Nathan
# Ik heb pressed_dict gemaakt, en het in de code gestoken ( bij on press, on release en start)
#For some reason werkt het niet aan jou om het uit te zoeken
#Groetjes, Verleden Nathan






import vgamepad as vg
import pynput
import mappings
import controller_buttons
import time

current_mapping=mappings.mario_kart     #Which mapping is used
lastX = None
lastY = None
gamepad = vg.VX360Gamepad()

#User mapping option
# if user_mapping == "Mario Kart 8 Deluxe":
#     current_mapping=mappings.mario_kart
# elif user_mapping == "custom1":
#     current_mapping=mappings.custom1
# elif user_mapping == "custom2":
#     current_mapping=mappings.custom2
# elif user_mapping == "custom3":
#     current_mapping=mappings.custom3


# def on_move(x, y):
#     global last_position
#     if last_position:
#         if x > last_position:
#             print('mouse moved right')
#         elif x < last_position:
#             print('mouse moved left')
#     last_position = x

#def on_move(x, y):
#   global lastX
#   global lastY
#   diffX= x-LastX
#   diffY= y-LastY
#   return diffX, diffY





def pressed_dict():             #Creates dictionary in which we can check if key is pressed
    pressed_dict={}
    for item in current_mapping:
        pressed_dict[item]=False
    return pressed_dict

def get_mapped_button(key):
    key_value = current_mapping[key]
    if key_value in controller_buttons.xbox:
        return controller_buttons.xbox[key_value]
    else: 
        print("the button this key is mapped to doesn't exist, please check mappings.py")

def on_press(key):
    global pressed_dict
    global two_pressed  #Boolean for ²
    if hasattr(key, 'char'):    #We check if key is a letter by checking char attribute                     Copy from here for releasing key
        if key.char in current_mapping:   #Configure letter Keys
            if not pressed_dict[key.char]:
                print(current_mapping[key.char])    #temporary code in place for VGamepad
                button_to_press = get_mapped_button(key.char)   #Conversion to make mappings.py more user-friendly
                if button_to_press:
                    gamepad.press_button(button=button_to_press)
                else:
                    print("If this is the first print something went wrong")
                gamepad.update()
                pressed_dict[key.char]=True
        if key.char == '²':
            two_pressed=True
    else:   #Key is special key
        if key in current_mapping:
            if not pressed_dict[key]:
                print(current_mapping[key])   
                button_to_press = get_mapped_button(key)
                if button_to_press:
                    gamepad.press_button(button=button_to_press)
                else:
                    print("If this is the first print something went wrong")
                gamepad.update()
                pressed_dict[key]=True                                                                  #Stop Copy
    if key == pynput.keyboard.Key.esc and two_pressed:            #If ² and Escape are pressed, we stop
        global time_to_stop
        time_to_stop=True
def on_release(key):
    global pressed_dict
    global two_pressed
    if hasattr(key, 'char'):
        if key.char == "²":
            two_pressed=False
    if hasattr(key, 'char'):    #We check if key is a letter by checking char attribute                     Copy from here for releasing key
        if key.char in current_mapping:   #Configure letter Keys
               #temporary code in place for VGamepad
            button_to_press = get_mapped_button(key.char)
            if button_to_press:
                gamepad.release_button(button=button_to_press)
            else:
                print("If this is the first print something went wrong")
            gamepad.update()
            pressed_dict[key.char]=False
    else:   #Key is special key
        if key in current_mapping:
               
            button_to_press = get_mapped_button(key)
            if button_to_press:
                gamepad.release_button(button=button_to_press)
            else:
                print("If this is the first print something went wrong")
            gamepad.update()    
            pressed_dict[key]=False
    print(f"{key} was released")

def start():
    global pressed_dict
    pressed_dict=pressed_dict()
    global two_pressed
    two_pressed = False
    listener = pynput.keyboard.Listener(on_press=on_press, on_release=on_release) #collect events
    listener.start()
    global time_to_stop
    time_to_stop=False
    running=True
    while running:
        
        if time_to_stop:     #Emergency Stop
            listener.stop()
            running=False
start()