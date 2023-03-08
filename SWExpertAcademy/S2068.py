# 삼성 2068 : 최대수 구하기
import sys ; input = sys.stdin.readline
t = int(input())
for i in range(1, t+1):
    aList = list(map(int,input().strip().split()))
    print("#{} {}".format(i, max(aList)))