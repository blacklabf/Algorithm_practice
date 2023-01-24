# 백준 ACM 호텔
# 수정한 풀이 (str -> int)
# 나누어 떨어지는 경우에 대해서 x,y 모두 차분하게 생각하기
import sys ; input = sys.stdin.readline
test = int(input().strip())
for i in range(test):
    a, b, c = map(int, input().strip().split())
    if c % a != 0:
        x = c % a 
        y = (c // a)+ 1
        print (x* 100 + y)
    else: 
        y = c // a
        print (a* 100 + y)