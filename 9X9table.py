# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 17:10:22 2018

@author: Administrator
"""
class Tablemult(object):
    def __init__(self):
        self.table9x9()

    def table9x9():
        for i in range(1,10):
            for j in range(1,i+1):
                print('%dX%d=%d'%(j,i,i*j),end='\t')
            print()
if __name__ =='__main__':
    Tablemult.table9x9()