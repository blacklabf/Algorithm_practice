# DFS와 BFS 1260
import sys; input = sys.stdin.readline
from collections import deque
queue = deque()

n, m, v = map(int,input().strip().split())

graph = [[] for _ in range(n+1)] 


for l in range(m):
	a, b = map(int, input().strip().split())
	graph[a].append(b)
	graph[b].append(a)
	
visited_d = [False] * (n+1)
visited_b= [False]* (n+1)

for k in range(1, n+1):
	graph[k].sort()

# DFS
def dfs(graph, v):
	visited_d[v]= True
	print(v,end=' ')
	for i in graph[v]:
		if not visited_d[i]:
			dfs(graph,i)

# BFS
def bfs(graph, v):
	queue.append(v)
	# queue = deque([v]) #v? -> deque에다가넣을 때 이렇게 넣음
	visited_b[v] = True
	while queue:
		a = queue.popleft()
		print(a,end=' ')
		for j in graph[a]:
			if not visited_b[j]:
				queue.append(j)
				visited_b[j] = True

dfs(graph,v)
print()
bfs(graph,v)
