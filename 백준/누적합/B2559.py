# 백준 2559 : 수열 (누적합)
import sys; input = sys.stdin.readline

n, k = map(int, input().strip().split())
nList = [0] + list(map(int, input().strip().split()))
preFix = [0] * (n+1)
ans = [0] * (n-k+2)

for i in range(1, n+1):
    preFix[i] = preFix[i-1] + nList[i]

for j in range(1, n-k+2):
    ans[j] = preFix[k+j-1] - preFix[j-1]


print(max(ans[1:]))