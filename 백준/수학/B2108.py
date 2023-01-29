# N이 홀수라고 가정하자
# 산술평균 - 평균 / 중앙값 : sort() 했을 때 중앙에 위치한 값 / 최빈값 : 제일 많이 나타나는 값 / 범위 : 최댓값과 최솟값의 차이
# count 쓰지 말기
# dictionary 사용법과 정렬, 값넣기

import math
import statistics
import sys ; input = sys.stdin.readline

N = int(input())
N_list = [int(input()) for _ in range(N)]
N_list.sort()

# 산술평균
print(round((sum(N_list))/N))

# 중앙값
print(N_list[math.trunc(N/2)])

# 최빈값
dic = {}
for num in N_list:
    if num not in dic:
        dic[num] = 1
    else:
        dic[num] = dic[num] + 1
sDic = sorted(dic.items(), key=lambda x:(-x[1], x[0]))
if len(sDic) > 1:
    if sDic[0][1] == sDic[1][1]:
        print(sDic[1][0])
    else :
        print(sDic[0][0])
else:
    print(sDic[0][0])

# 범위
num_max = max(N_list)
num_min = min(N_list)
print (num_max - num_min)