import sys ; input = sys.stdin.readline
n = int(input())
aList = []
for _ in range(n):
    aList.append(int(input()))
aList.sort()
print(*aList, sep='\n')