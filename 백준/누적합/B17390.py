# 백준 17390 : 이건 꼭 풀어야 해! (누적합)
import sys ; input = sys.stdin.readline
n, q = map(int, input().strip().split())
aList = [0] + list(map(int, input().strip().split()))
bList = sorted(aList)

preFix = [0] * (n+1)

for i in range(1, n+1):
    preFix[i] = bList[i] + preFix[i-1]

for i in range(q):
    a, b = map(int, input().strip().split())
    print(preFix[b]-preFix[a-1])
