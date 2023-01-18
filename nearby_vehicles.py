#!/usr/bin/python3
# coding: utf-8

'''
from _vehicle.py, found nearby vehicles with specified location
'''

import argparse
import math
from _vehicle import _VEHICLES, _PLAYER
from common import dist

class SearchNearby():
    def __init__(self, x, y, drange=100):
        self.range = drange
        self.x = x
        self.y = y
        self.results = {}
        self.ratio = [6*self.range, 6*self.range, 4*self.range, 3*self.range, 0]

    def show_results(self):
        ''' show results '''
        for k in sorted(self.results.keys()):
            p = self.results[k]
            r = float(k) / float(self.range) * len(self.ratio)
            r = int(r)
            print(k, p, dist.urlp(p, ratio=self.ratio[r]))

    def find_nearby_vehicles(self):
        ''' find nearby vehicles '''
        print(f'find_nearby_vehicles at {self.x},{self.y}, in range: {self.range}:')
        print('dist,', '(x,y),', 'url')
        self.results = {}
        for v in _VEHICLES:
            d = dist.dist(self.x, self.y, v[0], v[1])
            d = int(d)
            if d < self.range:
                self.results[d] = v

    def avg_xy(self):
        ''' avg of x, y location '''
        sumx = 0
        sumy = 0
        for v in _VEHICLES:
            sumx += v[0]
            sumy += v[1]
        avgx = int(sumx / len(_VEHICLES))
        avgy = int(sumy / len(_VEHICLES))
        print(f'I got avg center point at {avgx}, {avgy}')
        url = dist.url(avgx, avgy)
        print(url)


    def run(self):
        ''' run '''
        self.avg_xy()
        self.find_nearby_vehicles()
        self.show_results()

def main():
    ''' main '''
    # define argparse
    parser = argparse.ArgumentParser(description='Search nearby vehicles with specified location')
    parser.add_argument("coords", metavar='coords', type=int, nargs='*',
        help="specify location x and y")
    parser.add_argument('-d', '--dist', type=int, default=100,
        help='specify nearby range')
    parser.add_argument("-p", "--player", action='store_true', default=False,
        help="use player's location")

    (x, y) = (0, 0)
    arg = parser.parse_args()
    if arg.coords:
        x = arg.coords[0]
        y = arg.coords[1]
    else:
        x = _PLAYER[0]
        y = _PLAYER[1]
    search_nearby = SearchNearby(x, y, drange=arg.dist)
    search_nearby.run()

if __name__ == '__main__':
    main()
