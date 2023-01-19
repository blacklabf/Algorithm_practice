# N이 홀수라고 가정하자
# 산술평균 - 평균 / 중앙값 : sort() 했을 때 중앙에 위치한 값 / 최빈값 : 제일 많이 나타나는 값 / 범위 : 최댓값과 최솟값의 차이



# 시간초과 나왔는데 최빈값에서 count를 쓰면 안된다고 함



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
M_list = []
for i in range(N):
    M_list.append(N_list.count(N_list[i]))
a = max(M_list)
if M_list.count(a) == 2:
    print(N_list[M_list.index(a)])
elif N == 1:
    print(*N_list)
elif M_list.count(a) == N:
    print(N_list[1])
elif M_list.count(a) > 2 :
    del M_list[M_list.index(a)]
    del N_list[M_list.index(a)]
    del M_list[M_list.index(a)]
    del N_list[M_list.index(a)]
    print(N_list[M_list.index(a)])


M_list = []

for i in range(N):
    M_list.append(N_list.count(N_list[i]))

if M_list.count(max(M_list)) == 1:
    print(N_list[N-1])
else:
    print(N_list[N-2])

# 범위
num_max = max(N_list)
num_min = min(N_list)
print (num_max - num_min)


# 최빈값 수정 : 여러개면 두번째로 작은 값 출력
# N_list = [어떤 것들이 존재함]
# 최빈값이 1개인 경우
# statistics.mode(N_lsit)
# 최빈값이 2개 이상일 경우
# 
# 아이디어 - 



# import math
# import sys ; input = sys.stdin.readline

# N = int(input())
# N_list = [int(input()) for _ in range(N)]
# N_list.sort()

# print(round((sum(N_list))/N))

# print(N_list[math.trunc(N/2)])

# M_list = []
# for i in range(N):
#     M_list.append(N_list.count(N_list[i]))

# if M_list.count(max(M_list)) == 1:
#     print(N_list[N-1])
# else:
#     print(N_list[N-2])

# num_max = max(N_list)
# num_min = min(N_list)
# print (num_max - num_min)
