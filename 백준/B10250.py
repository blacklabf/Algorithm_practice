# 틀린 풀이
import sys ; input = sys.stdin.readline
test = int(input())
for i in range(test):
    a, b, c = map(int, input().strip().split())
    x = str(c % a) 
    y = str((c // a)+ 1)
    if len(y) == 1:
        y = '0' + y
    else : 
        pass
    print (x + y)