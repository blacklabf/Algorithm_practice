# import sys ; input = sys.stdin.readline

# N = int(input())

# # N_list = list(map(int, input().strip().split()) for _ in range(N))
# N_list = [input().strip().split() for _ in range(N)]
# print(N_list)
# final = sorted(N_list, key = lambda x : (x[0], x[1]))
# print(*final, sep='\n')


# N_list.sort(key = lambda (x: x[0], x[1]))
# print(*N_list)

# N_list = [map(int, input().strip().split()) for _ in range(N)] -> 이건 안됨.
# N_list = list(map(int, input().strip().split()) for _ in range(N))

# 오류코드
# N = int(input())
# N_list = []
# a, b = map(int, input().strip().split() for i in range(N))
# N_list.append([a,b])
# print(N_list)
# final = sorted(N_list, key = lambda x : (x[0], x[1]))
# print(*final, sep='\n')


import sys ; input = sys.stdin.readline
N = int(input())
N_list = []
for i in range(N):
    a ,b = map(int, input().strip().split())
    N_list.append([a, b])
final = sorted(N_list, key = lambda x : (x[0], x[1]))
for x, y in final:
    print(x, y)
# print(*final, sep='\n') -> 중복리스트의 리스트로 나옴