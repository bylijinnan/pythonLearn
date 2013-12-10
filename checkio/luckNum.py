#! /usr/bin/env python
# -*- coding: utf-8 -*-
# question: http://www.checkio.org/mission/task/info/mathematically-lucky-tickets/python-27/
# FileName is luckNum.py



DIFF = 1e-6 #0.000001

TARGET = 100 

def checkio(data):

    groups = splitToGroup(data)
    for g in groups:
        numbers = strListToNumList(g)
        expressions = g
        print "numbers = %s, expressions = %s" % (numbers, expressions)
        if canEqualsToTarget(numbers, expressions, len(numbers)):   #is not luck number
            return False
    return True
    
def splitToGroup(string):
    if len(string) == 1:
        return [[string]]
    
    result = []
    lastLetter = string[-1]
    groups = splitToGroup(string[:-1])
    for g in groups:
        g1 = g[:]
        g2 = g[:]
        g1.extend([lastLetter]) 
        result.append(g1)
        g2[-1] += lastLetter
        result.append(g2)
    return result


def canEqualsToTarget(numbers, expressions, n):
    if n == 1:
        diff = (numbers[0] - TARGET)
        #diff = abs(numbers[0] - TARGET)    #adding "abs" will cause endless loop. Why?
        print "diff = %f" % diff
        can = diff < DIFF
        if can: 
            print "equals, exp = %s" % expressions[0]
        return can

    for i in range(n):
        for j in range(i + 1, n):
            numA = (numbers[i])
            numB = (numbers[j])
            expA = expressions[i]
            expB = expressions[j]
        
            numbers[j] = numbers[n - 1]
            expressions[j] = expressions[n - 1]

            numbers[i] = numA + numB
            expressions[i] = "".join(["(", str(numA), "+", str(numB), ")"])
            if canEqualsToTarget(numbers, expressions, n - 1):
                return True

            numbers[i] = numA - numB
            expressions[i] = "".join(["(", str(numA), "-", str(numB), ")"])
            if canEqualsToTarget(numbers, expressions, n - 1):
                return True

            numbers[i] = numB - numA
            expressions[i] = "".join(["(", str(numB), "-", str(numA), ")"])
            if canEqualsToTarget(numbers, expressions, n - 1):
                return True

            numbers[i] = numA * numB
            expressions[i] = "".join(["(", str(numA), "*", str(numB), ")"])
            if canEqualsToTarget(numbers, expressions, n - 1):
                return True

            if (0.0 + numB) != 0:
                numbers[i] = numA / (0.0 + numB)
                expressions[i] = "".join(["(", str(numA), "/", str(numB), ")"])
                if canEqualsToTarget(numbers, expressions, n - 1):
                    return True

            if (0.0 + numA) != 0:
                numbers[i] = numB / (0.0 + numA)
                expressions[i] = "".join(["(", str(numB), "/", str(numA), ")"])
                if canEqualsToTarget(numbers, expressions, n - 1):
                    return True
            numbers[i] = numA
            numbers[j] = numB
            expressions[i] = expA
            expressions[j] = expB

    return False

def strListToNumList(strList):
    return [float(num) for num in strList] 
    
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('000000') == True, "All zeros"
    #assert checkio('707409') == True, "You can not transform it to 100"
    #assert checkio('595347') == False, "(5 + ((9 / (3 / 34)) - 7)) = 100"
    #assert checkio('271353') == False, "(2 - (7 * (((1 / 3) - 5) * 3))) = 100"

