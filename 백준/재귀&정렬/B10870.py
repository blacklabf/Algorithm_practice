# 백준 피보나치수 5
# 재귀를 이용한 풀이
def fibo(n):
    if n <=1:
        return n
    return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))