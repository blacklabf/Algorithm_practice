# 백준 숫자카드
# 여기서는 무조건 split 해야 함, str로 받으면 안됨
import sys; input = sys.stdin.readline
n = int(input()) # 숫자 카드의 개수
nList = list(map(int, input().strip().split())) # 상근이가 가지고 있는 숫자카드
m = int(input()) # 정수 M개
mList = list(map(int, input().strip().split())) # 상근이가 가지고 있는지 확인

ans = []

for num in mList:
    if num in nList:
        ans.append(1)
    else:
        ans.append(0)

print(*ans, sep=' ')



