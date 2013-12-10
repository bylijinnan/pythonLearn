#! /usr/bin/env python
# -*- coding: utf-8 -*-
# FileName is romanAndArabic.py
# see http://www.cnblogs.com/dosxp/archive/2008/08/13/1266781.html 

arabic = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
arabic_roman = dict(zip(arabic, roman))
roman_arabic = dict(zip(roman,arabic))

def checkio(number):
    'return roman numeral using the specified integer arabic from range 1...3999'
    
    return numberToRoman(number)
 
def numberToRoman(num):
    result = []
    base = 0
    while num != 0:
        index = 0
        times = 0
        while True:
            tmpBase = arabic[index]
            tmpTimes = num / tmpBase
            if tmpTimes:
                times = tmpTimes
                base = tmpBase
                num -= tmpBase * tmpTimes
                break
            index += 1
        result.append(arabic_roman[base] * times) 
        
    return "".join(result)
 
def romanToNumber(string):
    result = 0 
    previous = ""
    for cur in string:
        if cur not in roman:
            print "invalid input"
            return -1 
        if previous == "":
            result += roman_arabic[cur]
        else:
            if roman_arabic[cur] <= roman_arabic[previous]:
                result += roman_arabic[cur]
            else:
                result = result - 2 * roman_arabic[previous] + roman_arabic[cur]
        previous = cur 
    return result
            
    

if __name__ == '__main__':
    assert checkio(6) == 'VI', 'First'
    assert checkio(76) == 'LXXVI', 'Second'
    assert checkio(499) == 'CDXCIX', 'Third'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', 'Fourth'

    assert romanToNumber("VI") == 6, "1"
    assert romanToNumber("LXXVI") == 76, "2"
    assert romanToNumber("CDXCIX") == 499, "3"
    assert romanToNumber("MMMDCCCLXXXVIII") == 3888, "4"

    print 'All ok'
