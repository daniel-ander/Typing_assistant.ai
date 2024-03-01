#pip install pynput
#pip install pyperclip

from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
import time
import sys


controller = Controller()



def fix_current_line():
    pass

def fix_selection():
    #1. copy to clipboard
    with controller.pressed(Key.ctrl):
        controller.tap('c')
    #2. get the text from the clipboard
    time.sleep(.1)
    text = pyperclip.paste()
    print(text)
    #3. fix the text
    #4. paste the text back to the clipboard
#   pyperclip.copy('The text has been copied to the clipboard')
    #5. paste the text back to the editor




def on_f9():
    fix_current_line()

def on_f10():
    fix_selection()

def on_f11():
    sys.exit()
from pynput.keyboard import Key
with keyboard.GlobalHotKeys({
        '<120>': on_f9,
        '<121>': on_f10, 
        '<122>': on_f11}) as h:
    h.join()