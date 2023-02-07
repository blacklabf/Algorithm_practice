# K번째 수 11004
import sys ; input = sys.stdin.readline
n, k = map(int, input().strip().split())
nList = list(map(int, input().strip().split()))
nList.sort()
print(nList[k-1])