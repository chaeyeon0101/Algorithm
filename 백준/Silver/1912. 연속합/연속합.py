n = int(input())
data = list(map(int, input().split()))
d = [0] * n
d[0] = data[0]

for i in range(1, n):
    if d[i - 1] < 0:
        d[i] = data[i]
        continue
    d[i] = d[i - 1] + data[i]

print(max(d))