# 백준 11441 : 합 구하기 (누적 합)
import sys ; input = sys.stdin.readline
n = int(input())
# preFix : n+1로 하면 nList도 n+1개의 list를 해줘야 함!!!
nList = [0] + list(map(int, input().strip().split()))
m = int(input())
preFix = [0] * (n+1)
for i in range(1, n+1):
    preFix[i] = nList[i] + preFix[i-1]
for j in range(m):
    a, b = map(int, input().strip().split())
    print(preFix[b]-preFix[a-1])
