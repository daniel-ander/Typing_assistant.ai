# Text Correction Script

This script interacts with an Ollama server running a Mistral model to fix typos, casing, and punctuation in the text. It uses hotkeys to trigger the correction of the current line or selected text in the editor.

## Dependencies

The script relies on the following Python packages:

- `pynput`: Used to control and monitor input devices.
- `pyperclip`: A cross-platform Python module for copy and paste clipboard functions.
- `httpx`: A fully featured HTTP client for Python.
- `sys`: Provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter.
- `time`: Provides various time-related functions.

You can install these packages using pip:
pip install pynput pyperclip httpx sys time

## Mistral Instruct Server

The script relies on a local Ollama server running a Mistral model. Mistral is a language model developed by OpenAI. The specific model used in this script is `mistral:7b-instruct-v0.2-q4_K_S`.

The Ollama server should be running at `http://localhost:11434/api/generate`.

## Usage

The script defines three hotkeys:

- `F9`: Fixes the text of the current line in the editor.
- `F10`: Fixes the selected text in the editor.
- `F11`: Exits the script.

When you press `F9` or `F10`, the script copies the current line or selected text to the clipboard, sends it to the Ollama server for correction, and then pastes the corrected text back into the editor.

## Note

Please ensure that the Ollama server is running and accessible at the specified endpoint before running the script.
