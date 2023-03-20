from collections import deque
n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
d = [[-1, 1, 0, 0], [0, 0, -1, 1]]
answer = [0, 0]

def bfs(x, y):
    answer[0] += 1
    queue = deque([(x, y)])
    visited[x][y] = True

    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx, dy = x + d[0][i], y + d[1][i]
            if -1 < dx <n and -1 < dy < m and visited[dx][dy] == False and paper[dx][dy] == 1:
                queue.append((dx, dy))
                cnt += 1
                visited[dx][dy] = True
    if answer[1] < cnt:
        answer[1] = cnt

for i in range(n):
    for j in range(m):
        if visited[i][j] == False and paper[i][j] == 1:
            bfs(i, j)

print(answer[0])
print(answer[1])