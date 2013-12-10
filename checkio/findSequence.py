#! /usr/bin/env python
# -*- coding: utf-8 -*-
# FileName is findSequence.py
# http://www.checkio.org/mission/task/info/find-sequence/python-27/

def checkio(matr):
    '''
    Given the matrix NxN (4<=N<=10). Check if 4 numbers in sequence in a column or in a row or diagonally exist.
    '''
    
    count = 4
    
    #row
    for row in matr:
        if hasNumbersContinually(row, count):
            return True

    #column
    for column in zip(*matr):
        if hasNumbersContinually(column, count):
            return True

    #diagonally; two sides
    if hasInDiagonally(matr, count):
        return True
    
    return False

#斜线上是否有重复出现的数字；两个方向同时进行
def hasInDiagonally(matr, count):
    N = len(matr)
    #arr = [size][]
    slash_all = [[] for _ in range(N * 2 - 1)]
    backSlash_all = [[] for _ in range(N * 2 - 1)]
    k = 0
    for i in range(N):
        k = i
        for j in range(N):
            slash_all[k].append(matr[i][j])
            backSlash_all[k].append(matr[i][N - j - 1])
            k += 1
    all = slash_all
    all.extend(backSlash_all)
    for subList in all:
        if hasNumbersContinually(subList, count):
            return True
    return False
        
#序列是否连续且重复出现指定次数的数字（数字任意）            
def hasNumbersContinually(sequence, count):
    length = len(sequence)
    if length < count:
        return False
    for i in range(length - count + 1):
        flag = True
        for j in range(count):
            if sequence[i] != sequence[i + j]:
                flag = False
                break
        if flag:
            return True

    return False    
 

if __name__ == '__main__':
    assert checkio([
        [1, 1, 1, 1],
        [1, 2, 3, 4],
        [5, 4, 3, 1],
        [6, 1, 3, 2]
    ]) == True, "First, horizontal"
    assert checkio([
        [7, 6,  5, 7, 9],
        [8, 7,  3, 6, 5],
        [4, 0,  6, 5, 4],
        [9, 8,  4, 0, 5],
        [2, 10, 7, 2, 10]
    ]) == False, "Second"
    assert checkio([
        [10, 1, 9,  6, 4, 1],
        [2,  5, 4,  2, 2, 7],
        [2,  2, 1,  2, 6, 4],
        [3,  2, 2,  1, 0, 2],
        [7,  9, 6,  2, 5, 7],
        [7,  3, 10, 5, 6, 2]
    ]) == True, "Third"
    assert checkio([
        [6, 6, 7, 7, 7],
        [1, 7, 3, 6, 5],
        [4, 1, 2, 3, 2],
        [9, 0, 4, 0, 5],
        [2, 0, 7, 5, 10]
    ]) == False, "fourth"
    assert checkio([
        [1,  1, 1,  6, 1, 1, 1],
        [2,  5, 4,  2, 2, 7, 2],
        [2,  6, 1,  2, 6, 4, 3],
        [3,  2, 2,  1, 0, 2, 4],
        [7,  9, 6,  2, 5, 7, 5],
        [7,  3, 10, 5, 6, 2, 5],
        [7,  3, 10, 5, 6, 2, 5]
    ]) == False, "Fifth"
    assert checkio([
        [1, 1, 3, 1],
        [1, 2, 3, 4],
        [5, 4, 3, 1],
        [6, 1, 3, 2]
    ]) == True, "Six, vertircal"
