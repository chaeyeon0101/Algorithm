import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [False] * (n + 1)
t = 0
answer = 0
    
def dfs(x, d):
    global answer
    global t
    visited[x] = True
    graph[x].sort()
    t += 1
    answer += d * t
    for i in graph[x]:
        if visited[i] == False:
            dfs(i, d + 1)
        
dfs(r, 0)

print(answer)