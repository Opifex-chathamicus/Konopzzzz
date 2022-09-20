#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: XCS, L0WK3Y
"""
import os 

def run(**args):
    #retrieves any environment variables that are set on the remote machine.
    return str(os.environ)

if __name__ == '__main__':
    print(run())
