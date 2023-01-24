import sys
m = int(input())
s = set()

for _ in range(m):
    data = sys.stdin.readline().rstrip().split()
    
    if len(data) == 1:
        if data[0] == 'all':
            for i in range(1, 21):
                s.add(i)
        else:
            s = set()
        continue
    
    data[1] = int(data[1])
    
    if data[0] == 'add':
        s.add(data[1]);
    elif data[0] == 'remove':
        s.discard(data[1])
    elif data[0] == 'check':
        if data[1] in s:
            print(1)
        else:
            print(0)
    elif data[0] == 'toggle':
        if data[1] in s:
            s.discard(data[1])
        else:
            s.add(data[1])