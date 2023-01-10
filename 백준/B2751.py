# 내 제출 -> 시간초과
# N = int(input())
# N_list = [input() for _ in range(N)]
# print(*sorted(N_list), sep='\n')

# 마지막에 출력할 때 아래처럼 있던 코드를 간단하게 함
# N_list.sort()
# for i in N_list:
#     print(i)

# 최종 코드 
import sys; input = sys.stdin.readline
N = int(input())
N_list = [int(input()) for _ in range(N)]
print(*sorted(N_list),  sep='\n')
