#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 02:15:50 2021

@author: xcs
"""

import gitwrapper
import json
import os
import io, sys


#CONFIGURATION
konopas_id='msid_0'
konopas_config="%s.json"%konopas_id
path="config/"
path_filename=path+konopas_config
print(konopas_config)
print(path_filename)
konopas_modules=[]
configured=False
#

def main():
    token,headers=gitwrapper.login()
    get_konop_config(token,headers,path_filename)
    print(konopas_modules)
    path="modules/"
    for task in range(len(konopas_modules)):
        filename=konopas_modules[task]+".py"
        print("==========================================")
        print("\n"+filename+"\n")
        filepathname=path+filename
        resp,content=gitwrapper.get_file_contents(token,headers,filepathname)
        print(content)
        gitwrapper.write_to_file(filename,content) #writes to current directory
        #module=filename.strip(".py")
        #print(module)
        
        
        #keep a named handle on the prior stdout 
        old_stdout = sys.stdout 
        #keep a named handle on io.StringIO() buffer 
        new_stdout = io.StringIO() 
        #Redirect python stdout into the builtin io.StringIO() buffer 
        sys.stdout = new_stdout 
        
        exec(open(filename).read())
        #stdout from mycode is read into a variable
        result = sys.stdout.getvalue().strip()

        #put stdout back to normal 
        sys.stdout = old_stdout 
 
        print("result of "+filename+" is: '" + str(result) + "'") 

        

def get_konop_config(token,headers,path_filename):
    global configured
    resp,config_content=gitwrapper.get_file_contents(token,headers,path_filename)
    print(config_content)
    #config=json.loads(config_contentjs)
    #base64.b64decode(config_contentjs['content'])
    configured=True
    config=json.loads(config_content)
    for task in config:
            #print(task['module'])
            konopas_modules.append(task['module'])
            #exec("import %s" % task['module'])
    return config




main()
