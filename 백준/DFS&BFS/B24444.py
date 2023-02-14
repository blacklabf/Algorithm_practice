# 백준 24444 : 알고리즘 수업 - 너비우선탐색1 (BFS)
# 처음 출력값을 잘 못 이해함 
# 인덱스 출력으로 해서 시간 초과가 나옴
# timer로 해서 출력 => 그러면 방문 안 했을 경우에 대해 코드를 안 짜도 됨
import sys ; input = sys.stdin.readline
from collections import deque
queue = deque()
aList = []

def bfs(graph, visited, start):
    t = 1

    visited[start] = True
    queue.append(start)
    while queue :
        a = queue.popleft()
        
        timer[a] = t
        t += 1

        for i in graph[a]:
            if visited[i] == False :
                visited[i] = True
                queue.append(i)
                
    # 방문 안 했을 때 코드
    # for num in range(1, n+1):
    #     if visited[num] == False:
    #         print(0)

n, m, r = map(int, input().strip().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
aIdx = [[] for _ in range(n+1)]

# timer[x] = x번째 정점이 몇 번째로 방문되었는지
timer = [0] * (n + 1)

for j in range(1, m+1):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

for k in range(1, n+1):
    graph[k].sort()

bfs(graph, visited, r)

print(*timer[1:], sep="\n")
