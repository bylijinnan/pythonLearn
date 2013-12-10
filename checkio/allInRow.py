#! /usr/bin/env python
# -*- coding: utf-8 -*-
# FileName is allInRow.py
# http://www.checkio.org/mission/task/info/all-in-row/python-27/

import types

def checkio(arr):
    'convert all elements in arr in one row'
    
    return allInOneByRecursive(arr)
    #return allInOneTricky(arr)

#solution One
def allInOneByRecursive(list):
    if not hasSubList:
        return list
    
    allInOne = []
    for item in list:
        if type(item) == types.ListType:
            allInOne.extend(allInOneByRecursive(item))
        else:
            allInOne.append(item)
    return allInOne

def hasSubList(list):
    has = false    
    for item in list:
        if type(item) == types.ListType:
            has = true
            break
    return has
  
#solution 2. I think it's a little tricky
def allInOneTricky(arr):
    arrStr = str(arr)
    import re
    result = []
    nums = re.findall(r"\d+", arrStr)
    for num in nums:
        result.append(int(num))
    return result
    
if __name__ == '__main__':
    assert checkio([1,2,3]) == [1,2,3], 'First'
    assert checkio([1,[2,2,2],4]) == [1,2,2,2,4], 'Second'
    assert checkio([[[2]],[4,[5,6,[6],6,6,6],7]])\
                              == [2,4,5,6,6,6,6,6,7], 'Third'
    print 'All ok'
