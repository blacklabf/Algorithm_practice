# 백준 나이순정렬
# 수정한 풀이 : sorted -> sort / 나이는 int형으로 받음
# 인덱스는 따로 설정하지 않아도 들어간대로 나오기때문에 상관이 없지만 , append할 때 i를 추가해서 비교해줘도 됨.
import sys ; input = sys.stdin.readline
n = int(input())
nList = []
for _ in range(n):
    a, b = map(str, input().strip().split())
    nList.append([int(a), b])
nList.sort(key = lambda x : x[0])
for i in range(n):
    print(nList[i][0], nList[i][1])