import pynput

def on_press(key):
    print(f"{key} was pressed")
    if key == pynput.keyboard.Key.esc:
        global time_to_stop
        time_to_stop=True
def on_release(key):
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