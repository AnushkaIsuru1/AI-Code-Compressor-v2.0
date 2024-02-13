import tkinter as tk
from tkinter import *
from tkinter import filedialog
from time import time,sleep
import os
import pyperclip
import ctypes
#from base64fontinstall import *
from compressor import *
sys32 = ctypes.windll.user32

pgrnm = "CODE COMPRESSOR v.10"
uif = 'Saira SemiCondensed SemiBold'
cof = "menlo"
gc1 = "#23efbc"
gc2 = "#1eea7f"
gc3 = "#05342e"
gc4 = "#112537"
gc5 =  "#0c9c76"
gc6 = "#00705e"
gc7 = "#0f1426"
gc8 = "#000404"
gc9 = "#000003"
tgc1 = "#032a2b"
wc1 = "#fff"
wc2 = "#ddd"
wc3 = "#999"
twc1 = "#1e4255"
twc2 = "#204349"
twc3 = "#2f5366"
twc4 = "#316477"
rc1 = "#d40e2f"
rc2 = "#fe5060"
rc3 = "#500a20"
rc4 = "#4c0a1f"
bgc = "#010a0a"
hdc = gc1
blc = "#000000"


b1bg = bgc
b1fg = wc1
b1fo = ("arial",12)
b1w = 6
b1h = 1
b1px =10
b1py = 5

mw = Tk()
mw.title(pgrnm)
mw.configure(bg=bgc)
mw.minsize(width = 1200,height=720)
mw.maxsize(width = 1200,height=720)
