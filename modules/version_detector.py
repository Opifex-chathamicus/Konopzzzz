#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: XCS, L0WK3Y
"""

import sys

def run():
    version = sys.version
    ver_num = version.split(' ')
    return (str(ver_num[0]))

    
if __name__ == '__main__':
    print(run())