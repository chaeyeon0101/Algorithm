n,k=map(int,input().split())
data=[]

for i in range(n):
    data.append(int(input()))

coin=0
for i in range(n):
    if data[-(i+1)]<=k:
        coin=n-(i+1)
        break
    
answer=0;
while coin>-1:
    answer+=k//data[coin]
    k%=data[coin]
    coin-=1

print(answer)