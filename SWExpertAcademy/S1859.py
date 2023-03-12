# 삼성 1859 : 백만 장자 프로젝트
import sys; input = sys.stdin.readline
t = int(input())
for i in range(1, t+1):
    day = int(input())
    aList = list(map(int, input().strip().split()))
    ans = 0
    for j in range(day-1):
        if aList[j] < max(aList[j+1:]):
            ans += (max(aList[j+1:]) - aList[j])
    print('#{} {}'.format(i, ans))