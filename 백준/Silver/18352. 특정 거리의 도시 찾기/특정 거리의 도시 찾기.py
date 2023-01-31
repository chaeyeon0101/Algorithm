from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for i in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
answer = []
def bfs():
    queue = deque([x])
    visited[x] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = visited[v] + 1
                if visited[i] == k + 1:
                    answer.append(i)
                    continue
                queue.append(i)

bfs()

if answer:
    answer.sort()
    for i in answer:
        print(i)
else:
    print(-1)