# 백준 11724 : 연결 요소의 개수 (BFS)
import sys; input = sys.stdin.readline
from collections import deque
queue = deque()

def bfs(graph,visited,start):
    queue.append(start)
    visited[start]= True
    while queue:
        a = queue.popleft()
        # print(a, end=' ')
        for i in graph[a]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m = map(int, input().strip().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

# start
for j in range(1, m+1):
    a, b = map(int, input().strip().split())

    graph[a].append(b)
    graph[b].append(a)    

# bfs 실행
for num in range(1, n+1):
    if visited[num] == False:
        bfs(graph,visited,num)
        cnt += 1

print(cnt)