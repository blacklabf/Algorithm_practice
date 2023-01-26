# 수 정렬하기3
# 메모리초과
import sys ; input = sys.stdin.readline
n = int(input())
nList = []
for i in range(n):
    a = int(input())
    nList.append(a)
nList.sort()
print(*nList, sep = '\n' )