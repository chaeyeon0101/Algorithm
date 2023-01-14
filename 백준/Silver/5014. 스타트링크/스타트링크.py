from collections import deque

f, s, g, u, d = map(int, input().split())
visited = [0] * (f + 1)

def bfs():
    queue = deque()
    queue.append(s)
    visited[s] = 1
    
    while queue:
        x = queue.popleft()
        if x == g:
            return visited[g] - 1
        
        if x + u <= f and visited[x + u] == 0:
            queue.append(x + u)
            visited[x + u] = visited[x] + 1
        if x - d > 0 and visited[x - d] == 0:
            queue.append(x - d)
            visited[x - d] = visited[x] + 1
            
    return -1

answer = bfs()
if answer == -1:
    print("use the stairs")
else:
    print(answer)