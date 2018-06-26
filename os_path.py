# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 21:18:36 2018

@author: Administrator
"""

import os as o
def print_directory_contents(spath):
    for schild in o.listdir(spath):
        schildpath=o.path.join(spath,schild)
        try:
            if o.listdir(schildpath):
                print_directory_contents(schildpath)
            else:
                print(schildpath)
        except NotADirectoryError as n:
            print(schildpath)
        

print_directory_contents('F:\shiping')