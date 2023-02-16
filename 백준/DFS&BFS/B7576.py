# 백준 7576 : 토마토 (BFS)
import sys ; input = sys.stdin.readline
from collections import deque
queue = deque()

def bfs(graph,visited,startList):

    for i,j in startList:
        queue.append((i,j))
        visited[i][j] = True

    cnt = 0
    while queue:
        qSize = len(queue)

        for i in range(qSize):
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 1 or nx > n or ny < 1 or ny > m:
                    continue
                if graph[nx][ny] == 0 and visited[nx][ny] == False:
                    queue.append((nx,ny))
                    visited[nx][ny] = True
                    graph[nx][ny] = 1
        cnt += 1
    return cnt
        

m, n = map(int, input().strip().split())
graph = [[] ] 
visited = [[False] * (m+1) for i in range(n+1)]

dx = [-1, 0, 1, 0] # 시계방향
dy = [0, 1, 0, -1]

for j in range(1, n+1):
    graph.append([' '] + list(map(int, input().strip().split())))

startList = []
for i in range(1, n+1):
    for j in range(1, m+1):
        if graph[i][j] == 1:
            startList.append((i,j))

ans = bfs(graph, visited, startList)

flag = False
for i in range(1,n+1):
    for j in range(1, m+1):
        if graph[i][j] == 0:
            flag = True
if flag == True:
    print(-1)
else:
    print(ans-1)

# for i in range(1,n+1):
#     for j in range(1, m+1):
#         if graph[i][j] == 0:
#             flag = True
#             print(-1)
#             break
#     else:
#         print(ans-1)

# 50번째 줄 위에 flag = Fasle로 해줘도 되는데
# 위에처럼 if - break 랑 for- else문을 사용해도 됨.
# if flag == True:
#     print(-1)
# else:
#     print(ans-1)



# # visited로 하면 토마토가 없는 경우(-1)에도 True가 되므로 안됨
# print(visited)
# flag = False
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         if visited[i][j] == False:
#             print('###')
#             print((i,j))
#             flag = True
#             print(flag)
# if flag == True:
#     print(-1)
# else:
#     print(ans-1)







