# 백준 피보나치수
# Top - bottom
# 단순하게 재귀로만 하면 시간초과
import sys; input = sys.stdin.readline
n = int(input())

d = [0] * 46

def fibo(a):
    if a == 1:
        return 1
    elif a == 0:
        return 0
    elif d[a] != 0:
        return d[a]
    elif d[a] == 0:
        d[a] = fibo(a-1) + fibo(a-2)
        return d[a]
print(fibo(n))
