# 백준 2667 : 단지번호붙이기 (BFS)
import sys ; input = sys.stdin.readline
from collections import deque

def bfs(graph, visited, startX, startY):
	cnt = 0
	q = deque()
	
	q.append((startX, startY))
	visited[startX][startY] = True


	while q:
		x, y = q.popleft() 

		cnt += 1
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if nx < 1 or nx > n or ny < 1 or ny > n:
				continue
			
			if(visited[nx][ny] == False and graph[nx][ny] == 1):
				q.append((nx,ny))
				visited[nx][ny] = True

	return cnt

queue = deque()

n = int(input())

graph = [[]]
visited = [[False] * (n+1) for _ in range(n+1)]
cList = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = []

for i in range(1,n+1):
	graph.append([''] + list(map(int,list(input().strip()))))


# 1인 지점 탐색방법
for k in range(1, n+1):
	for l in range(1, n+1):
		if visited[k][l] == False and graph[k][l] == 1:
			answer.append(bfs(graph, visited ,k, l))

answer.sort()

print(len(answer))
for num in answer:
	print(num)








		








