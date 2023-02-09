# 백준 10867 : 중복 빼고 정렬하기
import sys ; input = sys.stdin.readline
n = int(input())
nList= list(map(int,input().strip().split()))
nList.sort() # set은 sort가 안돼서 list에서 먼저 sort 해줌
nSet = set(nList)
print(*nSet)