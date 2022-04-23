import pynput

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

def on_press(key):
    if hasattr(key, 'char'):
        if key.char:
            print("key.char")
    print(f"{key} was pressed")
    if key == pynput.keyboard.Key.esc:
        global time_to_stop
        time_to_stop=True
def on_release(key):
    if key in numpad_equivalents:
        key=numpad_equivalents[key]
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