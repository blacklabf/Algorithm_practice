import sys; input = sys.stdin.readline
a = []
n = int(input())
aList = list(map(int,input().strip().split()))
for i in range(n):
    a.append(abs(aList[i] - 320))
print(a.index(min(a)))

# 다른 풀이
n = int(input())
a = input().split() #문자열로 받으면 list로 됨

minDiff, minIndex = 1000, 0
for i in range(len(a)):
    diff = abs(int(a[i])-320)

    if minDiff >= diff:
        minDiff = diff
        minIndex = i
print(minIndex + 1)