# 백준 듣보잡 1764번
import sys ; input = sys.stdin.readline
n, m = map(int, input().strip().split())
aList = [input().strip() for i in range(n)]
bList = [input().strip() for j in range(m)]

aSet = set(aList)
bSet = set(bList)
abList = list(aSet & bSet)
abList.sort()

print(len(abList), *abList , sep='\n')