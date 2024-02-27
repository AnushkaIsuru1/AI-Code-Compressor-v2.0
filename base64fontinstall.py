import ctypes
import os
import shutil
import sys
from tkinter import *
from ctypes import wintypes
import base64
from datetime import datetime
try:
    import winreg
except ImportError:
    import _winreg as winreg

user32 = ctypes.WinDLL('user32', use_last_error=True)
gdi32 = ctypes.WinDLL('gdi32', use_last_error=True)

