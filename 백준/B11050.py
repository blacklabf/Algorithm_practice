# 내 풀이
import sys ; input = sys.stdin.readline
n, k = map(int, input().split())
def fac(a):
    num = 1
    if a == 0:
        num = 1
    else:
        for i in range(1, a+1):
            num = num * i
    return num

print(fac(n)//(fac(n-k)*fac(k)))

# for 문이용
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

result = 1
for i in range(K):
    result *= N
    N -= 1

divisor = 1
for i in range(2, K+1):
    divisor *= i

print(result // divisor)

# 재귀함수
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n-1)

# 조합 공식 nCk = n!/(n-k)!k!
print(factorial(N) // (factorial(N-K) * factorial(K)))