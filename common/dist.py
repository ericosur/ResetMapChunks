#!/usr/bin/python3
# coding: utf-8

import math

def dist(x1, y1, x2, y2):
    ''' dist '''
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return d

def distp(p1, p2):
    ''' dist two points '''
    d = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    return d
