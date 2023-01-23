# 백준 에디터
import sys ; input = sys.stdin.readline
from collections import deque 
str = list(input().strip())
m = int(input())
queue = deque()
for i in range(m):
    aList = list(input().strip().split())
    if 'L' in aList:
        if len(str) !=0:
            queue.appendleft(str.pop())
        else:
            pass
    elif 'D' in aList:
        if len(queue) != 0:
            str.append(queue.popleft())
        else: 
            pass
    elif 'B' in aList:
        if len(str) != 0:
            str.pop()
        else:
            pass
    elif 'P' in aList:
        str.append(aList[1])

print (*(str + list(queue)),sep='')
    



