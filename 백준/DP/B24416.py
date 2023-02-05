# 알고리즘 수업 - 피보나치 수 1
import sys ; input = sys.stdin.readline
a = int(input())

def fib(n):
    if n == 1 or n == 2:
        return 1
    else :
        return fib(n-1) + fib(n-2)

def fibonacci(n) :
    d = [0] * (n+1)
    d[1] = 1
    d[2] = 1
    dpcnt = 0
    
    for i in range(3, n+1):
        dpcnt += 1
        d[i] = d[i-1] + d[i-2]
    return dpcnt


print(fib(a) , fibonacci(a))