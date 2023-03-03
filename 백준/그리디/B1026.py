# 백준 1026 : 보물
# bList의 오름차순 정렬과 aList의 내림차순 정렬을 하면 됨
# 근데 bList는 건들면 안됨
# 이거는 그냥 문제의 조건이고 답이 나오게 하려면 문제풀때 정렬해도 상관없음 


import sys ; input = sys.stdin.readline
n= int(input())
aList = list(map(int, input().strip().split()))
bList = list(map(int,input().strip().split()))
aList.sort()
bList.sort(reverse=True)
num = 0
for i in range(n):
    num += (aList[i] * bList[i])
print(num)