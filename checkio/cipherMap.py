#! /usr/bin/env python
# -*- coding: utf-8 -*-
# FileName is cipherMap.py
# see http://www.checkio.org/mission/task/info/cipher-map/python-27/


# these codes are readable for me

def checkio(input_data):
    
    (flags, letters) = input_data
    size = len(flags[0])
    result = []
    for _ in range(4):
        result.extend([letters[i][j] for i in range(size) for j in range(size)
                       if flags[i][j] == "X"])
        flags = switch(flags, size)
    return "".join(result)


def switch(flags, size):
    result = []
    for i in range(size):
        one = "".join(flags[size -1 -j][i] for j in range(size))
        result.append(one)
        one = ""
    return result
        
        

if __name__ == '__main__':
    assert checkio([[
    'X...',
    '..X.',
    'X..X',
    '....'],[
    'itdf',
    'gdce',
    'aton',
    'qrdi']]) == 'icantforgetiddqd', 'First'

    assert checkio( [[
    '....',
    'X..X',
    '.X..',
    '...X'],[
    'xhwc',
    'rsqx',
    'xqzz',
    'fyzr']]) == 'rxqrwsfzxqxzhczy', 'Second'
    print('All ok')
