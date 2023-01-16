data = []
for _ in range(9):
    data.append(int(input()))
data.sort()
gap = sum(data) - 100

for i in range(9):
    for j in range(i + 1, 9):
        if data[i] + data[j] == gap:
            del data[j]
            del data[i]
            break
    
    if len(data) == 7:
        break

for i in data:
    print(i)