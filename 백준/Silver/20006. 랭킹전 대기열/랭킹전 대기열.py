p, m = map(int, input().split())
room = []
player = [input().split() for _ in range(p)]

for i in range(p):
    for j in range(len(room)):
        if room[j][0] - 10 <= int(player[i][0]) <= room[j][0] + 10 and room[j][1] < m:
            room[j][1] += 1
            player[i].append(j)
            break
    if len(player[i]) != 3:
        player[i].append(len(room))
        room.append([int(player[i][0]), 1])
            
player.sort(key = lambda x : (x[2], x[1]))

for i in range(len(room)):
    if room[i][1] == m:
        print("Started!")
    else:
        print("Waiting!")
    for j in range(room[i][1]):
        tmp = player.pop(0)
        print(tmp[0], tmp[1])