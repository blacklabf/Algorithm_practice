# ATM
import sys; input = sys.stdin.readline
n = int(input())
nList = list(map(int, input().strip().split()))
nList.sort()
count=0
for i in range(n):
    s = nList[i] * (n-i)
    count += s
print(count)