# 백준 바이러스 2606
import sys ; input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())


queue = deque()
#[[]*(n+1)] 과 [[] for _ in range(n)] 의 차이
graph = [[]  for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (n+1)



def bfs(graph, start , visited):
    queue.append(start)
    visited[start] = True
    cnt = 0
    while queue : 
        v = queue.popleft()
        cnt += 1
        # print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]= True
    print(cnt -1 )

bfs(graph, 1, visited)
