# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 22:08:16 2018

@author: lz
"""


class Febolaqi(object):
    def __init__(self):
        self.febo()

    def febo(self):
        a = 0
        b = 1
        while a < 1000:
            a, b = b, a + b
            # yield b
            print(a)


if __name__ == '__main__':
    Febolaqi.febo()