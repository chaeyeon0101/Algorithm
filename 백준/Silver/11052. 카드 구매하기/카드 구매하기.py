n = int(input())
p = list(map(int, input().split()))
p.insert(0, 0)
dp = [0] * (n + 1)
dp[1] = p[1]

for i in range(2, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + p[j])

print(dp[n])