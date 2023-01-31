# 백준 7894 큰 수
# 시간초과
import sys; input = sys.stdin.readline
t = int(input())

for i in range(t):
    a = int(input())
    b = 1
    for j in range(1, a+1):
        b *= j
    print(len(str(b)))