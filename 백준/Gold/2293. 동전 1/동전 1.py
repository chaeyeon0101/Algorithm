n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
coin.sort()
dp = [0] * (k + 1)
        
for i in coin:
    for j in range(coin[0], k + 1):
        if j - i <= 0:
            if j - i == 0:
                dp[i] += 1
            continue
        dp[j] += dp[j - i]

print(dp[k])