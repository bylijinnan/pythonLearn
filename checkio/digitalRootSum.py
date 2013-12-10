#! /usr/bin/env python
# -*- coding: utf-8 -*-
# FileName is digitalRootSum.py
# http://www.checkio.org/mission/task/info/digital-root-sum/python-27/

def checkio(value):
    'calculate sum of the digital roots of a numbers which are the results of factorization of the specified number'
    
    global allFactorList
    allFactorList = []
    findFactorList(value)
    return computeSum(allFactorList)


factorList = []
allFactorList = []

#递归求得所有的因式分解
def findFactorList(value):
    global factorList
    if value == 1:

        #无序时说明是重复的因式分解
        if isSortedList(factorList):
            allFactorList.append(factorList)
    else:
        for i in range(2, value + 1):

            #只需要计算到sqrt(value)，但value也是自身的一个因式分解
            if i != value and i * i > value:
                continue
            if value % i == 0:
                factorList.append(i)
                findFactorList(value / i)
                factorList = factorList[:-1]
   
def isSortedList(val):
    return sorted(val) == val
    
def computeSum(aList):
    result = 0
    for subList in aList:
        for num in subList:
            result += sumDigit(num)
    return result
    

def sumDigit(num):
    if num < 10:
        return num
    else:
        return sumDigit(reduce(lambda x,y:int(x) + int(y), str(num)))
    
if __name__ == '__main__':
    assert checkio(50) == 32, 'First'
    assert checkio(100) == 75, 'Second'
    assert checkio(999) == 75, 'Third'
    assert checkio(9999) == 117, 'Fourth'
    print 'All ok'


