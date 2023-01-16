import sys
n = int(input())
data = []
for _ in range(n):
    data.append(int(sys.stdin.readline().rstrip()))
data.sort()
    
result = []

result.append(round(sum(data) / n))
result.append(data[n // 2])

data_cnt = [[data[0], 1]]
for i in range(1, n):
    if data[i - 1] != data[i]:
        data_cnt.append([data[i], 1])
        continue
    data_cnt[len(data_cnt) - 1][1] += 1
data_cnt.sort(key=lambda x:-x[1])
if len(data_cnt) != 1 and data_cnt[0][1] == data_cnt[1][1]:
    result.append(data_cnt[1][0])
else:
    result.append(data_cnt[0][0])

result.append(max(data) - min(data))

for i in result:
    print(i)