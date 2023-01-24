# 백준 나이순정렬
# 틀린 풀이
n = int(input())
nList = [input().split() for _ in range(n)]
mList = sorted(nList, key = lambda x : x[0])
for i in range(n):
    print(mList[i][0], mList[i][1])