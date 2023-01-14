total = int(input())
target_a, target_b = map(int, input().split())
data_num = int(input())
data = [list(map(int,input().split())) for _ in range(data_num)]
visited = [False] * (total + 1)

def dfs(x):
    if visited[x]:
        return -1
    if target_b == x:
        return 0
    
    visited[x] = True
    for i in range(data_num):
        for j in range(2):
            if x == data[i][j]:
                tmp = dfs(data[i][j ^ 1])
                if tmp != -1:
                    return tmp + 1
    return -1
    
print(dfs(target_a))