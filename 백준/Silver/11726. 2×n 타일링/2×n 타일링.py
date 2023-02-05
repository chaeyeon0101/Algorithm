n = int(input())
dp = [1, 2]

while len(dp) < n:
    dp.append(sum(dp[-2 :]) % 10007)
    
print(dp[n - 1])