#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 15:27:19 2021

@author: xcs
"""

import konops

def main():
    konopas = konops.Konops("obsv")
    konopas.install_requirements()
    konopas.configure()
    #konopas.execute()

main()