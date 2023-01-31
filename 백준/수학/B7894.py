# 백준 7894 큰 수
# factorial , log , trunc라이브러리 사용

import sys; input = sys.stdin.readline
import math
t = int(input())

for i in range(t):
    a = int(input())
    b = math.factorial(a)
    c = math.log10(b)
    print(math.trunc(c) +1 )