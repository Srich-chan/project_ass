import system.lib.minescript as ms
import math
import time

DELTA = 1 / 20
EPS = 0.8

class Timer:
    def __init__(self, targ = -1):
        self.__t = time.time()
        self.__targ = targ
    def time(self):
        return time.time() - self.__t

    def is_ended(self):
        return self.__targ < self.time()

def dot_hor(v1, v2):
    return v1[0] * v2[0] + v1[2] * v2[2]

def is_near_hor(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[2]-p2[2]) < EPS
