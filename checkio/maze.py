#see http://www.checkio.org/mission/open-labyrinth/solve/

(E, S, W, N) = range(4)

class Node:
    "(x,y)=cell, d=direction. 这个NODE表示当你站在(x,y)这个位置时，下一步你可以住哪个方向(direction)走"
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
    
    def __str__(self):
        return "(%s, %s, %s)" % (self.x, self.y, self.d)
    
    
def checkio(maze):
    size = len(maze)
    (startX, startY) = (1, 1)
    (endX, endY) = (10, 10)
    
    stack = []
    
    #默认情况下，方向为未知(-1)
    stack.append(Node(startX, startY, -1))
    
    #设置为-1，表示这个cell已经走过，是路径的一部分了。避免重复踏上这个cell。
    maze[startX][startY] = -1
    
    while True:
        
        length = len(stack)
        if length <= 0:
            break
            
        curNode = stack[-1]
        
        #已经到达出口
        if (curNode.x == endX and curNode.y == endY):
            return formPath(stack)
            
        x = curNode.x
        y = curNode.y
        d = curNode.d
        
        #从E开始，顺时针方向查找下一个可行的方向
        d += 1
        find = False
        while d < 4:
            if d == E:
                x = stack[-1].x + 1
                y = stack[-1].y
            elif d == S:
                x = stack[-1].x
                y = stack[-1].y + 1
            elif d == W:
                x = stack[-1].x - 1
                y = stack[-1].y
            elif d == N:
                x = stack[-1].x
                y = stack[-1].y - 1
                
            #！！！注意表示水平方向的x和垂直方向的y，与矩阵下标的对应是反过来的
            #例如往北走，x不变，y减1（如上面的代码所示），对应矩阵是，列不变，往上一行
            #因此y是行坐标，x是列坐标
            if x >=0 and x < size and y >=0 and y < size and maze[y][x] == 0:
                find = True
                stack[-1].d = d
                stack.append(Node(x, y, -1))
                maze[y][x] = -1
                break
                
            d += 1
            
        #没有可行的路径，回退；将cell设置为“未踏入”，使得下一路径可以踏入
        if not find:
            n = stack[-1]
            maze[n.y][n.x] = 0
            stack = stack[:-1]
    
    print "no possibble path"
    return None

def formPath(aList):
    path = []
    d = {E:"E", S:"S", W:"W", N:"N"}
    for node in aList[:-1]:
        path.append(d[node.d])
    result = "".join(path)
    #print result
    return result
    

    
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]))
    #be carefull with infinity loop
    print(checkio([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]))
    print(checkio([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]))
