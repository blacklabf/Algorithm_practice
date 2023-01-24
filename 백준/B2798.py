# 백준 블랙잭
import sys; input = sys.stdin.readline
n, m = map(int, input().strip().split())
nList = list(map(int, input().strip().split())) 
result = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if nList[i] + nList[j] + nList[k] > m:
                continue
            else:
                result = max(result, nList[i]+nList[j]+nList[k])
print (result)