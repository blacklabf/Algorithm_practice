# 삼성 2070 : 큰 놈, 작은 놈, 같은 놈
import sys; input = sys.stdin.readline
t = int(input())
for i in range(1, t+1):
    a ,b = map(int, input().strip().split())
    if a > b :
        print('#{} >' .format(i))
    elif a < b :
        print('#{} <' .format(i))
    elif a == b :
        print('#{} =' .format(i))