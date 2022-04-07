import vgamepad as vg
import pynput
import mappings

current_mapping=mappings.mario_kart     #Which mapping is used
# last_position = None



# def on_move(x, y):
#     global last_position
#     if last_position:
#         if x > last_position:
#             print('mouse moved right')
#         elif x < last_position:
#             print('mouse moved left')
#     last_position = x
def on_press(key):
    global two_pressed  #Boolean for ²
    if hasattr(key, 'char'):    #We check if key is a letter by checking char attribute                     Copy from here for releasing key
        if key.char in current_mapping:   #Configure letter Keys
            print(current_mapping[key.char])    #temporary code in place for VGamepad
        if key.char == '²':
            two_pressed=True
    else:   #Key is special key
        if key in current_mapping:
            print(current_mapping[key])                                                                     #Stop Copy
    if key == pynput.keyboard.Key.esc and two_pressed:            #If ² and Escape are pressed, we stop
        global time_to_stop
        time_to_stop=True
def on_release(key):
    global two_pressed
    if hasattr(key, 'char'):
        two_pressed=False
    print(f"{key} was released")

def start():
    
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