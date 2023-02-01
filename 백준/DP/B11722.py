# 백준 가장 긴 감소하는 부분 수열 11722
import sys ; input = sys.stdin.readline
n = int(input())
nList = list(map(int, input().strip().split()))
mList = [] 
lenmList = []
for i in range(n):
    j = i+1
    line = [nList[i]]
    #while min(nList[i:]) != nList[i]:
    while j < n:
        if nList[i] > nList[j]:
            line.append(nList[j])
            i = j
            j = i + 1
        else:
            j += 1
    mList.append(line)
for j in range(n):
    lenmList.append(len(mList[j]))

print(max(lenmList))

