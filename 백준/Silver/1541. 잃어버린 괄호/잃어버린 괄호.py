n = input()

p = 0
answer = 0
total = 0

for i in range(len(n)):
    if i == len(n) - 1:
        total += int(n[p : ])
        answer += total
        print(answer)
        exit()
    if n[i].isdigit():
        continue
    total += int(n[p : i])
    p = i + 1
    if n[i] == "-":
        answer += total
        total = 0
        break

for i in range(p, len(n)):
    if n[i].isdigit():
        continue
    total += int(n[p : i])
    p = i + 1
    if n[i] == "-":
        answer -= total
        total = 0

total += int(n[p :])
answer -= total
print(answer)