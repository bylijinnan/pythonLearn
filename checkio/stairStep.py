#! /usr/bin/env python
# -*- coding: utf-8 -*-
# FileName is stairStep.py
# http://www.checkio.org/mission/task/info/stair-steps/python-27/

def checkio(stair_values):
    return findMax(stair_values)


def findMax(values):
    "use recursion"
    
    length = len(values)
    if length == 0:
        return 0
    if length == 1:
        return max(0, values[0])
    stepOnFirst = values[0] + findMax(values[1:])
    skipFirst = values[1] + findMax(values[2:])      #when you skip "firstStep", you must step on "secondStep"
    return max(stepOnFirst, skipFirst)
    
    
if __name__ == '__main__':
   assert checkio([5,6,-10,-7,4]) == 8, 'First'
   assert checkio([-11, 69, 77, -51, 23, 67, 35, 27, -25, 95])==393, 'Second'
   assert checkio([-21, -23, -69, -67, 1, 41, 97, 49, 27])==125, 'Third'
   assert checkio([5,-3,-1,2]) == 6, 'Fifth'
   print('All ok')

