import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(5)]
init_x, init_y = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, cnt, apple):
    if apple >= 2:
        return 1
    if x <= -1 or x >= 5 or y <= -1 or y >= 5 or cnt > 3:
        return 0
    if graph[x][y] == -1:
        return 0
    apple = apple + graph[x][y]
    graph[x][y] = -1
    for i in range(4):
        if dfs(x + dx[i], y + dy[i], cnt + 1, apple) == 1:
            return 1
    graph[x][y] = 0
    return 0
    
print(dfs(init_x, init_y, 0, 0))