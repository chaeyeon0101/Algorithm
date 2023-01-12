n=int(input())
data=list(map(int,input().split()))

data.sort()

answer=0
for i in range(n):
    answer+=(n-i)*data[i]

print(answer)