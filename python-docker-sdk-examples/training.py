#!/usr/bin/env python

"""AsyncioEx.py: Demo code for Async IO"""
__author__ = "Sumit Kala"

import time
import math

numlst = list(range(1, 9999999))
start = time.time()  # record wall clock time in seconds
newlst = []
for elem in numlst:
    newlst.append(math.sqrt(elem))
end = time.time()
# record wall clock time in seconds
print("Time Took = ", end - start)
start = time.time()
# record wall clock time in seconds
newlst = [math.sqrt(elem) for elem in numlst]
end = time.time()  # record wall clock time in seconds
print("Time Took = ", end - start)
start = time.time()  # record wall clock time in seconds
newlst = list(map(math.sqrt, numlst))
end = time.time()  # record wall clock time in seconds
print("Time Took = ", end - start)

import cProfile

numlst = list(range(1, 1001))


def fun1():


    newlst = []
for elem in numlst: newlst.append(elem * elem)


def fun2(): newlst = [elem * elem for elem in numlst]
# cProfile.run("fun1()") cProfile.run("fun2()") '''
# #comp:- #======= #>>math
