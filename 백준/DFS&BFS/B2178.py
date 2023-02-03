# 백준 미로탐색
# 10번째 줄에서 strip()을 꼭 해야 함.
import sys ; input = sys.stdin.readline
from collections import deque


n, m = map(int, input().split())
graph = [[]]
for i in range(n):
    graph.append([' '] + list(map(int, input().strip())))
#print(graph)

visited = [[False] * (m+1) for i in range(n+1)]

dx = [-1, 0, 1, 0] 
dy = [0, 1, 0, -1]

def bfs(x,y):
    queue= deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 1 or nx > n or ny < 1 or ny > m:
                    continue
                if graph[nx][ny] == 0:
                    continue
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))
    return graph[n][m]

print(bfs(1,1))
        






