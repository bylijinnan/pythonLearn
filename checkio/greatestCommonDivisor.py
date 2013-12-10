#! /usr/bin/env python
# -*- coding: utf-8 -*-
# FileName is greatestCommonDivisor.py

"""
 a | b means: b can be divided exactly by a
 m >= n
 m = nq + r
 a = gcd(m, n), b = gcd(n, r)
=> a | m && a | n
=> a | (m - nq)
=> a | r
=> a | r && a | n
=> a <= b (because b is "greatest")
...
so is b <= a
so a ==b

"""

def checkio(values):
    'Calculate the greatest common divisor of two numbers'
    #return  doInDivision(values)
    return doInRecursion(values)

def doInDivision(values):
    m, n = values
    if m < n:
        m, n = n, m
    while n != 0:
        r = m % n
        m, n = n, r
    return m

def doInRecursion(values):
    m, n = values
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    else:
        return doInRecursion((n, m % n)) 

if __name__ == '__main__':
    assert checkio((12, 8)) == 4, "First"
    assert checkio((14, 21)) == 7, "Second"
    assert checkio((13, 11)) == 1, "Third"
    print 'All ok'
    
