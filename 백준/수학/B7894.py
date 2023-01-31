# 백준 7894 큰 수
# 재귀 -> 백준에서는 1000번까지 가능인데 이 문제는 10^7만큼 해야해서 런타임에러

import sys; input = sys.stdin.readline
t = int(input())

def factori(a):
    if a > 1:
        return a * factori(a-1)
    else:
        return 1

for i in range(t):
    a = int(input())
    print(len(str(factori(a))))