# 삼성 2071 : 평균값 구하기
import sys; input = sys.stdin.readline
t = int(input())
for i in range(1, t+1):
    aList = list(map(int, input().strip().split()))
    avg = round(sum(aList) / 10 )
    print('#{} {}'.format(i, avg))