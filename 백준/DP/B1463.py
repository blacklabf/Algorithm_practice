# 1로 만들기 1463

import sys ; input = sys.stdin.readline

n = int(input())

d = [0] * (n+1)

for i in range(2, n+1):
    d[i] = d[i-1] + 1 # 1로 더하는 연산 (뺄셈 반대)
    if i % 6 == 0:
        d[i] = min(d[i], d[i//3]+1, d[i//2]+1)
    elif i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    elif i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
print(d[n])
    
    