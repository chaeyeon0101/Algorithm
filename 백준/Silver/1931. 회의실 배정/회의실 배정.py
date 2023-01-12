n=int(input())

data=[list(map(int,input().split())) for _ in range(n)]
data.sort(key=lambda x:(x[1],x[0]))

time=data[0][1]
answer=1
for i in range(1,n):
    if time<=data[i][0]:
        time=data[i][1]
        answer+=1

print(answer)