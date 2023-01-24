# 백준 숫자 카드 2
# 틀린 풀이 -> ans의 원소가 모두 0으로 나옴
import sys ; input = sys.stdin.readline
n = int(input().strip())
nList = input().strip().split()
m = int(input().strip())
mList = list(map(int, input().strip().split()))


ans =[0]* m
for i in range(m):
    for mNum in mList:
        if mNum in nList:
            ans[i] = nList.count('mNum')
        else:
            pass

print(*ans)

