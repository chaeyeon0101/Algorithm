switch_num=int(input())
switch=list(map(int,input().split()))
switch.insert(0, -1)
student_num=int(input())
student=[list(map(int,input().split())) for _ in range(student_num)]

for i in range(student_num):
    if student[i][0]==1:
        num=student[i][1]
        while(num<=switch_num):
            switch[num] ^= 1
            num+=student[i][1]
    elif student[i][0]==2:
        switch[student[i][1]] ^= 1
        num=1
        while student[i][1]-num>=1 and student[i][1]+num<=switch_num:
            if switch[student[i][1]-num]!=switch[student[i][1]+num]:
                break
            switch[student[i][1]-num] ^= 1
            switch[student[i][1]+num] ^= 1
            num+=1
            
for i in range(1, switch_num+1):
    print(switch[i], end=" ")
    if i%20 == 0:
        print()