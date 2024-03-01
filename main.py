# Dependencies: pynput, pyperclip, httpx, sys, time 
#pip install pynput pyperclip httpx sys time

# This script interacts with an Ollama server running a Mistral model to fix typos, casing, and punctuation in the text.
# ollama run mistral:7b-instruct-v0.2-q4_K_S
'''
This code performs the following tasks:

#1 Importing necessary dependencies: pynput, pyperclip, httpx, sys, and time.
#2 Defining the OLLAMA endpoint and configuration for connecting to a local OLLAMA server.
#3 Creating a template for the prompt to be sent to the OLLAMA server.
#4 Implementing a function fix_text() that sends a prompt to the OLLAMA server and returns the corrected text.
#5 Implementing a function fix_current_line() that fixes the text of the current line in the editor.
#6 Implementing a function fix_selection() that fixes the selected text in the editor.
#7 Defining event handlers for the F9, F10, and F11 keys.
#8 Setting up global hotkeys for the F9, F10, and F11 keys using the pynput library.
#9 Starting the event listener to capture the key presses and execute the corresponding functions.

'''
from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
import time
import sys
import httpx
from string import Template


controller = Controller()

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
OLLAMA_CONFIG = {"model": "mistral:7b-instruct-v0.2-q4_K_S",
                "keep_alive": "5m",
                "stream": False
}

PROMPT_TEMPLATE = Template(
    """Fix all typos and casing and punctuation in this text, but preserve all new line characters: 
    
    $text 
    
    Return only the corrected text, don't include a preface or preamble.
    
    """
)
def fix_text(text):
    prompt = PROMPT_TEMPLATE.substitute(text=text)
    response = httpx.post(OLLAMA_ENDPOINT, json={"prompt": prompt, **OLLAMA_CONFIG}, 
                          headers={"Content-Type": "application/json"}, 
                          timeout=10)
    if response.status_code != 200:
        print("Error: ", response.status_code, response.text)
        return None
    return response.json()["response"].strip()


def fix_current_line():
    #shift + home
    controller.press(Key.shift)
    controller.press(Key.home)

    controller.release(Key.shift)
    controller.release(Key.home)

    fix_selection()


def fix_selection():

    #1. copy to clipboard


    with controller.pressed(Key.ctrl):
        controller.tap('c')
    #2. get the text from the clipboard
        
    time.sleep(.2)
    text = pyperclip.paste()
    print(text)

    #3. fix the text

    fixed_text = fix_text(text)

    #4. paste the text back to the clipboard
    pyperclip.copy(fixed_text)
    time.sleep(.2)


#   pyperclip.copy('The text has been copied to the clipboard')
    #5. paste the text back to the editor

    with controller.pressed(Key.ctrl):
        controller.tap('v')




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
        '<119>': on_f11}) as h:
    h.join()