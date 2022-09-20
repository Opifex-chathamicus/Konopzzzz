#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 00:19:10 2021
@author: xcs
"""

import requests
import base64
import json


API_URL="https://api.github.com"


def login():
    tokenfd = open("./data/mytoken.txt",'r')
    token=tokenfd.readline().strip()
    tokenfd.close()
    headers={
        "Authorization":"token "+token,
        "Accept":"application/vnd.github.v3+json"
        }
    return token,headers
    
#####################################################################
#######################GET REPO CONTENTS #############################

def get_repo_contents(token,headers):
    r=requests.get(API_URL+"/repos/Opifex-chathamicus/Konopzzzz/contents/modules/",headers=headers)
    #print(r2.json())
    counts=len(r.json())
    resp=r.json()
    files=[]
    for i in range(counts):
        files.append(resp[i]['name'])
        print(resp[i]['name'],":")
        print(resp[i]['sha'])
        print("=========================================================")
    
###########################################################################
####################### GET FILE CONTENTS #################################

def get_file_contents(token,headers,path_filename):
    path="/repos/Opifex-chathamicus/Konopzzzz/contents/"
    r=requests.get(API_URL+path+path_filename,headers=headers)
    resp=r.json()
    #print(resp) #to identify if we our API rate limit exceeded
    contentresp=resp['content']
    contentresp=base64.b64decode(contentresp)
    contentresp=str(contentresp.decode("UTF-8")) #the base64 decoded data has to be converted from bytes to string
    return resp,contentresp

###########################################################################
####################### WRITE LOCALLY TO FILE #############################                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
def write_to_file(filename,content): 
    modname=filename
    modfd=open("./"+modname,'w')
    modfd.write(content)
    modfd.close()


###########################################################################
####################### POST TO GITHUB ###################################

#Create or update file contents
#Creates a new file or replaces an existing file in a repository.
#put /repos/{owner}/{repo}/contents/{path}

def store_to_file(token,headers,path_filename,commit,content): #to data folder
    path="/repos/Opifex-chathamicus/Konopzzzz/contents/"
    contentb64unm=str(base64.b64encode(content.encode("utf-8"))) 
    contentb64=contentb64unm.strip('b').strip("'") 
    data={"message":commit,"content":contentb64}
    datajson=json.dumps(data)
    r=requests.put(API_URL+path+path_filename,data=datajson,headers=headers)
    resp=r.json()
    return resp