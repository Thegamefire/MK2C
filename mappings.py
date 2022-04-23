# This file is for mapping keyboard inputs to controller outputs
from pynput.keyboard import Key
# custom1={}
# custom2={}
# custom3={}

testing={
    "Mouse_Right_Stick": True,
    Key.shift :"A",    #Drive
    's' :"B",
    'q' : "LeftStickLeft",
    'z' : "LeftStickUp"
}


mario_kart={
    "z":"LeftStickUp",
    "q":"LeftStickLeft",
    "s":"LeftStickDown",
    "d":"LeftStickRight",

    Key.shift:"B",
    Key.ctrl_l:"A",
    Key.alt_l:"Y",

    "NumPad5": "LB",
    Key.space:"RB",
    Key.esc:"START"
}
