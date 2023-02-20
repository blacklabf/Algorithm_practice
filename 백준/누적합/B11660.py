# 백준 11660 : 구간합구하기5 (누적합)
# 행 별로 누적합 list를 다시 만들어줌 
import sys ; input = sys.stdin.readline

n, m = map(int, input().strip().split())
nList = [0] * (n+1)
# preFix = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    nList[i] = [0] + list(map(int,input().strip().split()))

# 여기서 preFix도 2차원 배열이라 각 행의 첫번째 열에 대해서 다시 해줌
# for k in range(1, n+1):
#     for l in range(1, n+1):
#         preFix[k][l] = preFix[k][l-1] + nList[k][l]


# for j in range(m):
#     a, b, c, d = map(int,input().strip().split())
#     if a==c and b==d:
#         print(nList[a][b])
#     else:
#         ans = 0
#         for num in range(a, c+1):   
#             ans = ans + (preFix[num][d] - preFix[num][b-1])
            
#         print(ans)
            



    
# 누적합으로 안한다면
for j in range(m):
    a, b, c, d = map(int,input().strip().split())
    ans = 0
    for k in range(a, c+1):
        for j in range(b, d+1):
            ans = ans + nList[k][j]
    print(ans)


