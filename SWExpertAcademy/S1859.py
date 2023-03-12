# 삼성 1859 : 백만 장자 프로젝트
import sys; input = sys.stdin.readline
t = int(input())
for i in range(1, t+1):
    day = int(input())
    aList = list(map(int, input().strip().split()))
    ans = 0
    max_val = aList[-1] # aList의 마지막 값 / 이전의 최댓값
    for j in range(day-2, -1 , -1):
        if aList[j] < max_val :
            ans += (max_val - aList[j])
        else :
            max_val = aList[j] # 최댓값 갱신
    print('#{} {}'.format(i, ans))