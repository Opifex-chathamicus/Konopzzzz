#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: XCS, L0WK3Y
"""
import os

def run(**args):

    files = os.listdir(".") #lists all files in current directory
    return str(files)

if __name__ == '__main__':
    print(run())
