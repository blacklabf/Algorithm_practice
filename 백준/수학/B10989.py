# 메모리 초과
# N = int(input())
# num_list = []
# for i in range(N):
#     num = int(input())
#     num_list.append(num)
# print(*sorted(num_list), sep='\n')

import sys ; input = sys.stdin.readline
N = int(input())
N_list = [int(input()) for _ in range(N)]
print(*sorted(N_list), sep='\n')

