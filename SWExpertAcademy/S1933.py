# 삼성 1933 : 간단한 N의 약수
import sys; input = sys.stdin.readline
n = int(input())
ans = []
for i in range(1, n+1):
    if n % i == 0 :
        ans.append(i)
    else :
        pass
print(*ans, end=' ')