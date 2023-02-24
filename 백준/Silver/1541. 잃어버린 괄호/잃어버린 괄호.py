n = input()

p = 0
answer = 0
total = 0

for i in range(len(n)):
    if n[i] == "-":
        total += int(n[p : i])
        answer += total
        total = 0
        p = i + 1
        break
    elif n[i] == "+":
        answer += int(n[p : i])
        p = i + 1
    if i == len(n) - 1:
        answer += int(n[p :])
        print(answer)
        exit()

for i in range(p, len(n)):
    if n[i] == "-":
        total += int(n[p : i])
        answer -= total
        total = 0
        p = i + 1
    elif n[i] == "+":
        total += int(n[p : i])
        p = i + 1

total += int(n[p :])
answer -= total
print(answer)