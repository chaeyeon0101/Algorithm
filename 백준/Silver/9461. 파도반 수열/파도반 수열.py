t = int(input())
p = [0, 1, 1, 1, 2, 2]

for _ in range(t):
    n = int(input())
    
    if len(p) <= n:
        for i in range(len(p), n + 1):
            p.append(p[i - 1] + p[i - 5])
    
    print(p[n])