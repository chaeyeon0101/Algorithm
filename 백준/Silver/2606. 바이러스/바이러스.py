from collections import deque

num = int(input())
data_num = int(input())
data = [[] for _ in range(num + 1)]
for _ in range(data_num):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)
visited = [False] * (num + 1)

queue = deque([1])
visited[1] = True

cnt = 0
while queue:
    x = queue.popleft()
    
    for i in data[x]:
        if not visited[i]:
            queue.append(i)
            cnt += 1
            visited[i] = True
            
print(cnt)