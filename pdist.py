#!/usr/bin/python3
# coding: utf-8

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
    else:
        print("not cygwin")

if __name__ == '__main__':
    main()
