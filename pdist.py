#!/usr/bin/python3
# coding: utf-8

import os
from common import dist
import myutil

def test_dist():
    ''' test dist '''
    p1 = (7055, 8142)
    p2 = (7526, 8582)
    d = dist.distp(p1, p2)
    print(f'{p1} - {p2} -> {d:.3f}')

def test_platform():
    ''' test platform '''

def main():
    ''' main '''
    if myutil.is_cygwin():
        print("cygwin")
    elif myutil.is_linux():
        print("linux")
    elif myutil.is_windows():
        print("windows")
    else:
        print("I donno...")

    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

if __name__ == '__main__':
    main()
