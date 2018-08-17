#This setup file is used to convert that script in to exe
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os","win32com.client","speech_recognition","Time","wolframalpha","pygame","pyttsx3","pyperclip"], "excludes": ["tkinter"]} # give full path of driver
# GUI applications require a different base on Windows (the default is for a
# console application).
'''base = None
if sys.platform == "win32":
    base = "Win32GUI" ''' # by erase 3 inverted comma from both lines you will make exe without console, or for console make it disabble.

setup(  name = "Name what u want",
        version = "0.1",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("AI -Voice Command Bot.py", base=base)])    

