#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: XCS, L0WK3Y
"""

import sys

#https://docs.python.org/3/library/sys.html

def run():
    if hasattr(sys, 'real_prefix'):
        return "Virtual Machine: True"
    else:
        return "Virtual Machine: False"

if __name__ == '__main__':
    print(run())