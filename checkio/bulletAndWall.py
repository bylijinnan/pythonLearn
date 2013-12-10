#! /usr/bin/env python
# -*- coding: utf-8 -*-
# FileName is bulletAndWall.py
# see http://www.checkio.org/mission/task/info/bullet-and-wall/python-27/ 

def checkio(data):
    xw1, yw1 = data[0]
    xw2, yw2 = data[1]
    xa, ya = data[2]
    xb, yb = data[3]

    (a1, b1, c1) = abc(data[0], data[1])
    (a2, b2, c2) = abc(data[2], data[3])
    
    parallel = (a1 * b2 == a2 * b1)    
    
    #平行
    if parallel:
        #同一直线，判断方向是否正确
        if a1 * c2 == a2 * c1 and inSameDirection(xa, ya, xb, yb, xw2, yw2):
            return True
        else:
            return False
            
    #不平行，求交点。若交点满足以下两个条件，则返回True:
    #1.点在目标线段上
    #2.点在向量的方向上
    else:
        my = a2 * b1 - a1 * b2
        mx = -my
        y = (a1 * c2 - a2 * c1) / (my + 0.0)
        x = (b1 * c2 - b2 * c1) / (mx + 0.0)
        return isPointIncluded(xw1, yw1, xw2, yw2, x, y) and inSameDirection(xa, ya, xb, yb, x, y)
        
#点(x, y)是否在线段(点a, 点b)上
def isPointIncluded(xa, ya, xb, yb, x, y):
    minx = min(xa, xb)
    maxx = max(xa, xb)
    miny = min(ya, yb)
    maxy = max(ya, yb)
    return  minx <= x <= maxx and miny <= y <= maxy

#向量（A->B），求点(x, y)是否在向量的前方
def inSameDirection(xa, ya, xb, yb, x, y):
    return (x - xa) * (xb - xa) >=0 and (y - ya) * (yb - ya) >=0

#根据两点求出直线的方程ax + by + c = 0
def abc(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    a = y2 - y1
    b = x1 - x2
    c = y1 * (x2 - x1) - (y2 - y1) * x1
    return (a, b, c)


if __name__ == '__main__':
    assert checkio([[0,0], [0,2], [5,1], [3,1]]) == True, "First"
    assert checkio([[0, 0], [0, 2], [3, 1], [5, 1]]) == False, "Reverse First"
    assert checkio([[0, 0], [2, 2], [6, 0], [3, 1]]) == True, "Second"
    assert checkio([[6, 0], [5, 5], [4, 0], [5, 6]]) == False, "Third"
    assert checkio([[0, 0], [1, 1], [3, 3], [2, 2]]) == True, "Fourth, shot in butt of wall :)"
    assert checkio([[0, 0], [1, 1], [3, 2], [2, 1]]) == False, "Fifth, parallel"

