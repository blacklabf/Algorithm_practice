# 삼성 2029 : 몫과 나머지 출력하기
import sys; input = sys.stdin.readline
t = int(input())
for i in range(1, t+1): 
    a, b = map(int, input().strip().split())
    quo = a // b
    rem = a % b
    print('#{} {} {}'.format(i, quo, rem))