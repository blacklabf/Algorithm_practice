# 백준 1012 : 유기농 배추 (BFS)
import sys ; input = sys.stdin.readline
from collections import deque
queue = deque()


def bfs(graph, visited, startX, startY):
    queue.append((startX, startY))
    visited[startX][startY] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1 : # n,m이 바뀜
                continue
            if visited[nx][ny] == False and graph[nx][ny] == 1 :
                queue.append((nx,ny))
                visited[nx][ny] = True
    

t = int(input())
for _ in range(t):
    m, n, k = map(int,input().strip().split())
    graph = [[0]*(m) for _ in range(n)]
    visited = [[False] * (m) for _ in range(n)]
    dx = [-1, 0 , 1, 0]
    dy = [0, 1, 0 , -1]
    cnt = 0
    for j in range(k):
        a, b =map(int, input().strip().split())
        graph[b][a] = 1 #a가 m 안에 범위고 n이 n 안의 범위이므로 

    # start
    for num in range(n):
        for nums in range(m):
            if visited[num][nums] == False and graph[num][nums] == 1:
                bfs(graph, visited, num , nums)
                
                cnt +=1
    print(cnt)
    





    
