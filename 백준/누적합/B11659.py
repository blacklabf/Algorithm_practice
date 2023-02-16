# 백준 11659 : 구간합구하기4 (누적합)
import sys ; input = sys.stdin.readline
n, m = map(int, input().strip().split())
preFix = [0] * (n+1)
nList = [0] + list(map(int,input().strip().split()))
for i in range(1, n+1):
    preFix[i] = nList[i] + preFix[i-1]
for j in range(m):
    a, b = map(int, input().strip().split())
    sum = preFix[b] - preFix[a-1]
    print(sum)