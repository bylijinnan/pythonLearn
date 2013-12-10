#! /usr/bin/env python
# -*- coding: utf-8 -*-
# FileName is twoArraysBalance.py
# see http://www.checkio.org/mission/task/info/batteries-loading/python-27/

def checkio(stones):
    '''
    minimal possible weight difference between stone piles
    '''
    length = len(stones)
    if length == 0:
        return 0
    if  length == 1:
        return stones[0]
    if length == 2:
        return abs(stones[0] - stones[1])
        
    import itertools
    result = 0
    all = sum(stones)
    half = all / 2
    for lenn in range(length):
        firstPart = min(itertools.combinations(stones, lenn), key = lambda x:abs(sum(x) - half))
        firstPartSum = sum(firstPart)
        diff = abs(all - firstPartSum - firstPartSum)
        if lenn == 0:
            result = diff
        elif diff < result:
            result = diff
    return result
            
        
        
    
    
if __name__ == '__main__':
    assert checkio([10,10]) == 0, 'First, with equal weights'
    assert checkio([10]) == 10, 'Second, with a single stone'
    assert checkio([5, 8, 13, 27, 14]) == 3, 'Third'
    assert checkio([5,5,6,5]) == 1, 'Fourth'
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, 'Fifth'
    assert checkio([1, 1, 1, 3]) == 0, "Six, don't forget - you can hold different quantity of parts"
    print 'All is ok'
