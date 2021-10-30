#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 14:10:26 2021

@author: XCS, L0WK3Y
"""

import os

def run(**args):

    print("[*]In the dirlister module.")

    files = os.listdir(".") #lists all files in current directory
    return str(files)

if __name__ == '__main__':
    run()
