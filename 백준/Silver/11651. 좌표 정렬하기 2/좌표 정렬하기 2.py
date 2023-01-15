n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
data.sort(key=lambda x:(x[1],x[0]))

for i in range(n):
    for j in data[i]:
        print(j, end = ' ')
    print()