n_cnt = [0] * 10
n = input()

total = 0
for i in range(10):
    n_cnt[i] = n.count(str(i))
    total += n_cnt[i] * i

if n_cnt[0] != 0 and total % 3 == 0:
    for i in range(9, -1, -1):
        for j in range(n_cnt[i]):
            print(i, end = '')
else:
    print(-1)