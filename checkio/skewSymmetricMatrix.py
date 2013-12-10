#! /usr/bin/env python
# -*- coding: utf-8 -*-
# FileName is skewSymmetricMatrix.py
# http://www.checkio.org/mission/task/info/skew-symmetric-matrix/python-27/

def checkio(matr):
    return map(lambda x:map(lambda n:-n, x), zip(*matr)) == matr

if __name__ == '__main__':
    assert checkio(
             [[0, 1,2],
             [-1,0,1],
             [-2,-1,0]]) == True, 'First'
    assert checkio(
             [[0, 1,2],
             [-1,1,1],
             [-2,-1,0]]) == False, 'Second'
    assert checkio(
             [[0, 1,2],
             [-1,0,1],
             [-3,-1,0]]) == False, 'Third'
    print 'All ok'
