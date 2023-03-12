# 삼성 2019 : 더블더블
import sys; input = sys.stdin.readline
n = int(input())
#for i in range(n+1):
#    print(2**i, end=' ')
ans = [2**i for i in range(n+1)]
print(*ans)