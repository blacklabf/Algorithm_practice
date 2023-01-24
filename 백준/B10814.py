# 백준 나이순정렬
# 틀린 풀이 2 : 나이를 int형으로 받고 출력해야 함.
n = int(input())
nList = [input().split() for _ in range(n)]
nList.sort(key = lambda x : x[0])
for i in range(n):
    print(int(nList[i][0]), nList[i][1])