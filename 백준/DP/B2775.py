# 부녀회장이 될테야
import sys ; input = sys.stdin.readline
# a층 b호에 살려면 a-1층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 해
# k와 n에 대해 k층에 n호에는 몇명이 살고 있는지
# 0층부터 있고 0층 i호에는 i명이 살고 
t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    d = [ [0] * (n+1) for j in range(k+1)]
    for q in range(n+1):
        d[0][q] = q
    for p in range(k+1):
        d[p][1] = 1
    for a in range(1, k+1):
        for b in range(1, n+1):
            d[a][b] = d[a][b-1] + d[a-1][b]
    print(d[k][n])