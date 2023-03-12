# 삼성 2043 : 서랍의 비밀번호
import sys; input = sys.stdin.readline
p, k = map(int, input().strip().split())
cnt = 1
while p != k:
    k += 1
    cnt += 1
print(cnt)

# .. k가 p보다 크거나 같을 경우 고려
if p == k : 
    print(1)
elif p > k :
    print(p-k+1)
else:
    print(999-k+1+p)