#! /usr/bin/env python
# -*- coding: utf-8 -*-
# FileName is pageCounter.py
# http://www.checkio.org/mission/task/info/page-counter/python-27

def checkio(data):
    'return the number of pages'
    
    height = data['height']
    width = data['width']
    text = data['text']
    
    if text == "" or len(text) <= width:
        return 1
        
    pageCount = 0
    lineCount = 0
    
    longWord = False
    while True:
        length = len(text)
        if length == 0:
            break
        
        if length <= width:
            lineCount += 1
            break
        
        newStart = 0
        if text[width - 1]  == " ":
            newStart = width
        elif text[width]  == " ":
            newStart = width + 1
        else:
            spaceIndex = findPreviousSpace(text, width - 1)
            if spaceIndex < 0:
                newStart = width
                longWord = True
            else:
                newStart = spaceIndex + 1
                if longWord:
                    longWord = False
        lineCount += 1
        text = text[newStart:]
    
    lineCount += data['text'].count("\n")
    pageCount = lineCount / height
    if lineCount % height != 0:
        pageCount += 1
    return pageCount
    
# not found:return -1
def findPreviousSpace(text, curIndex):
    spaceIndex = curIndex
    while True:
        if spaceIndex == -1:
            break
        if text[spaceIndex] == " ":
            break
        spaceIndex -= 1
    return spaceIndex

if __name__ == '__main__':
    assert checkio({'height':3,
             'width':5,
             'text': 'It\'s boooooooorrrrrrriiiiiinnnnggggg dude'
    }) == 3, 'With a one long word'
    assert checkio({'height':3,
             'width':5,
             'text': 'To be or not to be'
    }) == 2 , 'From description'
    
    assert checkio({'height':1,
             'width':5,
             'text': 'HI'
    }) == 1, 'with single sort word'
    
    assert checkio({'height':1,
             'width':5,
             'text': 'hello'
    }) == 1, 'with signle word with long as width'
    
    assert checkio({'height':3,
             'width':5,
             'text': ''
    }) == 1, 'one page for no words'
    
    
    assert  checkio({'height':3,
             'width':5,
             'text': '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Cras hendrerit enim ultricies justo tincidunt ut auctor ipsum hendrerit. Phasellus ultricies dolor eu arcu auctor a rutrum enim tristique. 
Phasellus purus odio, pharetra in sodales vel, adipiscing eget libero. Quisque rhoncus urna at ipsum tincidunt facilisis. In vitae diam dolor. 
Nullam eleifend aliquam porttitor. Curabitur viverra malesuada eleifend. Fusce eu dui quis neque accumsan consectetur id id metus. 
Cras rutrum purus sed massa malesuada in consequat augue viverra. Vestibulum consectetur lacinia commodo. 
Phasellus urna nisi, tincidunt a ullamcorper egestas, iaculis sed mauris.'''
    }) == 49 , 'Lorem ipsum'
    
    
    'All ok :)'

