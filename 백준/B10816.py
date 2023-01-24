# 백준 숫자 카드 2
# 수정한 풀이 -> 이것도 ans가 0으로만 나옴
import sys ; input = sys.stdin.readline
n = int(input().strip())
nList = list(map(int, input().strip().split()))
m = int(input().strip())
mList = list(map(int, input().strip().split()))



ans =[0]* m
for i in range(m):
    if mList[i] in nList:
        ans[i] = nList.count(mList[i])
    else:
        pass

print(*ans)
