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

FONTS_REG_PATH = r'Software\Microsoft\Windows NT\CurrentVersion\Fonts'

HWND_BROADCAST = 0xFFFF
SMTO_ABORTIFHUNG = 0x0002
WM_FONTCHANGE = 0x001D
GFRI_DESCRIPTION = 1
GFRI_ISTRUETYPE = 3

if not hasattr(wintypes, 'LPDWORD'):
    wintypes.LPDWORD = ctypes.POINTER(wintypes.DWORD)

user32.SendMessageTimeoutW.restype = wintypes.LPVOID
user32.SendMessageTimeoutW.argtypes = (
    wintypes.HWND,   # hWnd
    wintypes.UINT,   # Msg
    wintypes.LPVOID, # wParam
    wintypes.LPVOID, # lParam
    wintypes.UINT,   # fuFlags
    wintypes.UINT,   # uTimeout
    wintypes.LPVOID  # lpdwResult
)

gdi32.AddFontResourceW.argtypes = (
    wintypes.LPCWSTR,) # lpszFilename

