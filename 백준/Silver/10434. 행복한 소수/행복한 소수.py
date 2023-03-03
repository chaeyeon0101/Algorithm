import sys
import math
input = sys.stdin.readline
p = int(input())
prime_num = [True] * 10001
prime_num[0] = [False]
prime_num[1] = [False]
visited = [0] * 10001

def beHappy(x):
    if x == 1:
        return 1
    if visited[x] == 0:
        visited[x] = -1
        tmp = 0
        for i in str(x):
            tmp += int(i) ** 2
        visited[x] = beHappy(tmp)
    return visited[x]
            
for i in range(2, int(10000 ** 0.5) + 1):
    if prime_num[i] == True:
        for j in range(i + i, 10001, i):
            prime_num[j] = False

for _ in range(p):
    a, b = map(int, input().split())
    if prime_num[b] == False:
        print(a, b, "NO")
        continue
    
    beHappy(b)
    
    if visited[b] == 1:
        print(a, b, "YES")
    else:
        print(a, b, "NO")