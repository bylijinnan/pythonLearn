#! /usr/bin/env python
# -*- coding: utf-8 -*-
# FileName is numberToEnglish
#http://www.checkio.org/mission/task/info/speechmodule/python-27/


FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] 
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    
    print "number = ", number
    
    if (number < 0 or number > 999):
        print "invalid input"
        return ""
    
    if number < 10:
        return FIRST_TEN[number]
    if number >=   10 and number < 20:
        return SECOND_TEN[number - 10]
        
    result = ""    
    
    while True:
        
        if number == 0:
            break
        if number < 20:
            result += " " + checkio(number)
            break
            
        length = len(str(number))
        base = 10 ** (length - 1)
        num = number / base
        
        if (num == 0):
            continue
        
        if length == 3:
            result += FIRST_TEN[num] + " " + HUNDRED
        elif length == 2:
                result += " " + OTHER_TENS[num - 2]
        number %= base
        length = len(str(number))
    return result.strip()
        
        
    
if __name__ == '__main__':
    assert checkio(4) == 'four', "First"
    assert checkio(133) == 'one hundred thirty three', "Second"
    assert checkio(12)=='twelve', "Third"
    assert checkio(101)=='one hundred one', "Fifth"
    assert checkio(212)=='two hundred twelve', "Sixth"
    assert checkio(40)=='forty', "Seventh, forty - it is correct"

    print 'All ok'
