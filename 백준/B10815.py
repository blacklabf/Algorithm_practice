# 백준 숫자카드 10815번 이진탐색 풀이
import sys ; input = sys.stdin.readline

n = int(input())
nList = list(map(int, input().strip().split()))
m = int(input())
mList = list(map(int, input().strip().split()))
answer = []

nList.sort()

def lower_bound(arr, val):
    lo = 0
    hi = len(nList)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < val :
            lo = mid + 1
        else:
            hi = mid
    return lo

for x in mList:
    idx = lower_bound(nList, x)
    if idx < n and nList[idx] == x:
        answer.append(1)
    else:
        answer.append(0)

print(*answer, sep=' ')

