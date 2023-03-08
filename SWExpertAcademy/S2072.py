# 삼성 2072 : 홀수만 더하기 
import sys ; input = sys.stdin.readline
t = int(input())
for i in range(1, t+1):
    aList = list(map(int, input().strip().split()))
    odd = 0
    for num in aList:
        if num % 2 == 1:
            odd += num
    print("#{} {}".format(i, odd))