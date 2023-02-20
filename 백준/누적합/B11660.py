# 백준 11660 : 구간합구하기5 (누적합)
import sys ; input = sys.stdin.readline

n, m = map(int, input().strip().split())
nList = [0] * (n+1)
preFix = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    nList[i] = [0] + list(map(int,input().strip().split()))

# 여기서 preFix도 2차원 배열이라 각 행의 첫번째 열에 대해서 다시 해줌
for k in range(1, n+1):
    for l in range(1, n+1):
        if l == 1:
            preFix[k][l] = nList[k][l] + preFix[k-1][n]
        else : 
            preFix[k][l] = nList[k][l] + preFix[k][l-1]

for j in range(m):
    a ,b ,c, d = map(int,input().strip().split())
    # 2차원 배열이라 그 전 preFix를 뺄 떄 인덱스를 어떻게 할 지 고민
    print(preFix[c][d] - preFix[a][b] + nList[a][b])

