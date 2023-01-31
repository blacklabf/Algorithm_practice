# 백준 7894 큰 수
# 라이브러리 사용
# factorial을 구해주면 값이 커져서 시간초과 -> log 곱셈 성질 이용

import sys; input = sys.stdin.readline
import math
t = int(input())

for i in range(t):
    a = int(input())
    s = 0
    for j in range(1, a+1):
        s += math.log10(j)
    print(math.trunc(s) +1)