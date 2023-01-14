from collections import deque
n, m, v = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
for i in range(m):
    graph[i].sort()
graph.sort(key = lambda x : (x[0], x[1]))

def dfs(x):
    if visited[x]:
        return
    
    visited[x] = True
    print(x, end=' ')
    for i in range(m):
        for j in range(2):
            if x == graph[i][j]:
                dfs(graph[i][j ^ 1])
    return

def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = True
    
    while queue:
        nx = queue.popleft()
        print(nx, end = ' ')
        for i in range(m):
            for j in range(2):
                if nx == graph[i][j] and visited[graph[i][j ^ 1]] == False:
                    queue.append(graph[i][j ^ 1])
                    visited[graph[i][j ^ 1]] = True

visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)