# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:03:06 2018

@author: lz
"""
import random
class rand10(object):
    def __init__(self):
        self.rd10()
        self.listlv()
        
    def listlv(self,*arg):
        sum1=0
        list_b=[]
        for i in arg:
            sum1+=i
        print(sum1)
        for j in arg:
            list_b.append(format(round(j/sum1,5),'.3%'))
        return list_b
    
    def rd10(self):
        list_a=[0,0,0,0,0,0,0,0,0,0]
        n=0
        while n<10000:
            sign=random.randint(1,10)
            list_a[sign-1]+=1
            n+=1
        listfinal=rand10.listlv(*list_a)
        print(listfinal)
    
if __name__=='__main__':
    rand10()