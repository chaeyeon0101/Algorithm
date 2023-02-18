from collections import deque

n = int(input())
arr = [input() for _ in range(n)]
visited = [[False] * n for _ in range(n)]
d = [[-1, 1, 0, 0], [0, 0, -1, 1]]

def dfs(i, j):
    queue = deque([(i, j)])
    visited[i][j] = True
    
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            dx, dy = x + d[0][k], y + d[1][k]
            if -1 < dx < n and -1 < dy < n:
                if visited[dx][dy] == False and arr[dx][dy] == arr[i][j]:
                    queue.append((dx, dy))
                    visited[dx][dy] = True
                    
def rg_b_dfs(i, j):
    queue = deque([(i, j)])
    visited[i][j] = True
    
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            dx, dy = x + d[0][k], y + d[1][k]
            if -1 < dx < n and -1 < dy < n:
                if visited[dx][dy] == False:
                    if arr[i][j] == 'B':
                        if arr[dx][dy] == arr[i][j]:
                            queue.append((dx, dy))
                            visited[dx][dy] = True
                    else:
                        if arr[dx][dy] != 'B':
                            queue.append((dx, dy))
                            visited[dx][dy] = True

cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            cnt += 1
print(cnt, end = " ")

cnt = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            rg_b_dfs(i, j)
            cnt += 1
print(cnt)