#!/usr/bin/python3
# coding: utf-8

import math

_MAP_URL = 'https://map.projectzomboid.com/'

def dist(x1, y1, x2, y2):
    ''' dist '''
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return d

def distp(p1, p2):
    ''' dist two points '''
    d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    return d

def url(x1, y1):
    ''' compose url '''
    return f'{_MAP_URL}#{x1}x{y1}'

def urlp(p, ratio=200):
    ''' compose p '''
    r = ''
    if ratio == 0 or ratio > 2400:
        r = f'{_MAP_URL}#{p[0]}x{p[1]}x200'
    else:
        r = f'{_MAP_URL}#{p[0]}x{p[1]}x{ratio}'
    return r
