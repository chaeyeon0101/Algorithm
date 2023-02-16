from collections import deque
import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
visited = [[False] * n for _ in range(m)]
for _ in range(k):
    a, b, c, d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d):
            visited[j][i] = True
d = [[-1, 1, 0, 0],[0, 0, -1, 1]]

def bfs(j, i):
    queue = deque([(i, j)])
    visited[i][j] = True
    
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for l in range(4):
            dx, dy = x + d[0][l], y + d[1][l]
            if 0 > dx or dx >= m or 0 > dy or dy >= n:
                continue
            if visited[dx][dy]:
                continue
            queue.append((dx, dy))
            cnt += 1
            visited[dx][dy] = True
    return cnt

answer = []            
for i in range(m):
    for j in range(n):
        if visited[i][j] == False:
            answer.append(bfs(j, i))
answer.sort()
print(len(answer))
print(*answer)