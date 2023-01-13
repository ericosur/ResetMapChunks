#!/usr/bin/python3
# coding: utf-8

'''
only backup different files
'''

from os import environ, system
from os.path import split as path_split, abspath, join, isfile
import sys

HOME= environ.get('HOME')
SRC1 = HOME + '/' + 'Downloads/zomboid/save1/20221126-survivor'
SRC2 = HOME + '/' + 'Downloads/zomboid/save2/20221126-survivor'

class Solution():
    ''' class to do diff backup '''
    def __init__(self):

    def run(self):
        ''' run '''


def main():
    ''' main '''
    ofile = 'diff-report.txt'
    cmd = f'diff -qr {SRC1} {SRC2} > {ofile}'
    print(cmd)
    system(cmd)

if __name__ == '__main__':
    main()
