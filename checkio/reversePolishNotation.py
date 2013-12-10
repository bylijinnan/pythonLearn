#! /usr/bin/env python
# -*- coding: utf-8 -*-
# FileName is reversePolishNotation.py

operator = {"#":-1, "(":0, ")":0, "+":1, "-":1, "*":2, "/":2, "^":3}

def isHigher(opA, opB):
    return operator[opA] > operator[opB]
  
"""
#replace it by aList[-1]  
def peek(aList):
    return aList[len(aList) -1]
"""

def checkio(expression):
    'transform the expression'
    
    if not expression:
        print "invalid input"
        return ""
    
    result = []
    stack = ["#"]
    
    for ele in expression:
        
        if ele not in operator:
            result.append(ele)
            continue
            
        if ele == "(":
            stack.append(ele)
            continue
        
        if ele == ")":
            while stack[-1] != "(":
                result.append(stack.pop())
            stack.pop()     #discard "("
            continue
            
        top = stack[-1]
        if top == "(":
            stack.append(ele)
            continue
            
        if isHigher(ele, top):
            stack.append(ele)
        else:
            while True:
                top = stack.pop()
                if top == "(":
                    break
                if isHigher(ele, top):
                    stack.append(top)
                    stack.append(ele)
                    break
                result.append(top)
    
    #the expression is finished
    if stack:
        
        #delete the first "#" and reverse 
        rStack = stack[1:][::-1]
        
        result.extend(rStack)
        
    return "".join(result)

    
if __name__ == '__main__':
    assert checkio('a+b') == 'ab+', 'First'
    assert checkio('((a+b)*(z+x))') == 'ab+zx+*', 'Second'
    assert checkio('((a+t)*((b+(a+c))^(c+d)))') == 'at+bac++cd+^*', 'Third'
    assert checkio('a+b*c+d') == 'abc*+d+' , 'Fourth'
    'All ok'
