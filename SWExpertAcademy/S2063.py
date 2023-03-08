# 삼성 2063 : 중간값 찾기
import sys ; input = sys.stdin.readline
n = int(input())
nList = list(map(int,input().strip().split()))
mList = sorted(nList)
k = ((n+1)//2) -1
print(mList[k])