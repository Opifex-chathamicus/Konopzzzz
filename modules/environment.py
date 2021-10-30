#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 14:10:26 2021

@author: XCS, L0WK3Y
"""
import os 

def run(**args):
    #retrieves any environment variables that are set on the remote machine.
    print("[*] In environment module.")
    print(str(os.environ))
    return str(os.environ)

if __name__ == '__main__':
    run()
