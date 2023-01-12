n=int(input())

answer=0
i=n//5
while i>-1:
    tmp_n=n
    tmp_n=n-5*i
    if(tmp_n%3==0):
        answer+=i
        answer+=tmp_n//3
        break
    i-=1

if answer==0:
    answer=-1

print(answer)