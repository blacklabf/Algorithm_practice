# 백준 피보나치 함수 1003
# fibo(0) -> 0을 출력하고 0을 리턴
# fibo(1) -> 1을 출력하고 1을 리턴
# fibo(2)
import sys ; input = sys.stdin.readline
t = int(input())

for i in range(t):
    a = int(input())
    d = [0] * 41
    z = [0] * 41
    o = [0] * 41
    d[0] = 0 ; d[1] = 1
    z[0] = 1 ; z[1] = 0
    o[0] = 0 ; o[1] = 1
    for j in range(2, a+1):
        d[j] = d[j-1] + d[j-2]
        z[j] = z[j-1] + z[j-2]
        o[j] = o[j-1] + o[j-2]
    print(z[a], o[a])