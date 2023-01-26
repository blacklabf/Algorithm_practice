# 백준 피보나치수 5
# for문을 이용한 풀이
import sys ; input = sys.stdin.readline
n = int(input())
fibo = []
for i in range(n+1):
    if i == 0:
        fibo.append(0)
    elif i == 1:
        fibo.append(1)
    elif i >=2 :
        fibo.append(fibo[i-2]+fibo[i-1])
print(fibo[n])