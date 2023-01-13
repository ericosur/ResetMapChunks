#!/usr/bin/python3
# coding: utf-8

from common import dist

def main():
    p1 = (7055, 8142)
    p2 = (7526, 8582)
    d = dist.distp(p1, p2)
    print(f'{p1} - {p2} -> {d:.3f}')

if __name__ == '__main__':
    main()
