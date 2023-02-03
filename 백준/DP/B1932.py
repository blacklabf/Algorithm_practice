# 백준 정수 삼각형 
import sys ; input = sys.stdin.readline

n = int(input())
tri = []

for i in range(n):
    tri.append(list(map(int,input().strip().split())))
    if i >= 1:
        for j in range(i+1):
            if j == 0:
                tri[i][j] = tri[i][j] + tri[i-1][j]
            elif j == i :
                tri[i][j] = tri[i][j] + tri[i-1][j-1]
            else :
                tri[i][j] = tri[i][j] + max(tri[i-1][j-1], tri[i-1][j])
print(*tri, sep='\n')
print(max(tri[n-1]))

# depth = int(input())

# nums = []

# for i in range(depth):
#     nums.append(list(map(int,input().split())))

# for i in range(1,depth):
#     for j in range(len(nums[i])):
#         if j == 0:
#             nums[i][j] = nums[i][j] + nums[i-1][j] #가장 왼쪽은 자기상단의 수와 합
#         elif j == len(nums[i]) - 1:
#             nums[i][j] = nums[i][j] + nums[i-1][j-1] #가장 오른쪽은 자기 상단의 수와 합
#         else:
#             nums[i][j] = max(nums[i-1][j-1],nums[i-1][j]) + nums[i][j] #중간수들은 상단의 두개중 큰수와 합
# print(max(nums[depth-1])) #depth의 마지막 배열중 가장 큰수 도출