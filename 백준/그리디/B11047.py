# 백준 11047 : 동전O(그리디)

import sys ; input = sys.stdin.readline

n, k = map(int, input().strip().split())
aList = []
cnt = 0

for i in range(n):
    aList.append(int(input()))

bList = aList [::-1]
j = len(aList)

for b in range(j):
    if bList[b] > k :
        continue
    elif k == 0:
        break
    else:
        cnt += ( k // bList[b])
        k = k % bList[b]

print(cnt)

# 여기서 인덱스를 뒤집어서 새로운 리스트를 만들지 말고 reversed(range(n))을 해서 for문을 돌려주면 되고
# aList의 길이를 구해서 j를 놓지 말고 처음 입력값인 n 이 j와 같은 역할을 한다. 

