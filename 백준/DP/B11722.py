# 백준 가장 긴 감소하는 부분 수열 11722
# dp -> i번째 까지의 가장 긴 감소하는 수열을 저장을 해줌
import sys ; input = sys.stdin.readline
n = int(input())
nList = list(map(int, input().strip().split()))
dP = [1] * (n+1) 
for i in range(n):
    for j in range(i):
        if nList[j] > nList[i]: 
            dP[i] = max(dP[j]+1, dP[i])
print(max(dP))





