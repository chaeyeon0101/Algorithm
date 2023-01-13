n=int(input())
data=[list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    cnt=0
    for j in range(n):
        if i!=j and data[i][0]<data[j][0] and data[i][1]<data[j][1]:
            cnt+=1
    data[i].append(cnt)

for i in range(n):
    print(data[i][2]+1, end=" ")