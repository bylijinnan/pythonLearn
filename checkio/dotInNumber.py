#! /usr/bin/env python
# -*- coding: utf-8 -*-
# FileName is dotInNumber.py
# http://www.checkio.org/mission/task/info/dot-separated-numbers/python-27/ 

import re


def checkio(txt):
    '''
    string with dot separated numbers, which inserted after every third digit from right to left
    '''

    # the best solution is ==> return re.sub(r'(?<=\d)(?=(\d\d\d)+\b)', '.', str(txt))

    numbers = findNumber(txt)
    if numbers:
        for n in numbers:
            txt = txt.replace(n, addDotToNumber(n))
    return txt
    

def findNumber(txt):
    return re.findall(r"\b\d+(?!th)\b", txt)
    
def addDotToNumber(numStr):
    result = numStr
    if len(result) > 3:
        length = len(result)
        result = addDotToNumber(result[:length -3]) + "." + result[length - 3:length]; 
    return result


"""
def checkio(txt):

"""
if __name__ == '__main__':
    assert checkio('123456') == '123.456'
    assert checkio('333') == '333'
    assert checkio('9999999') == '9.999.999'
    assert checkio('123456 567890') == '123.456 567.890'
    assert checkio('price is 5799') == 'price is 5.799'
    assert checkio('he was born in 1966th') == 'he was born in 1966th'
    print 'All ok'
    

