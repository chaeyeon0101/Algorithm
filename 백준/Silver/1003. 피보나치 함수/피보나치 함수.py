t = int(input())
dp = []
dp.append([1, 0])
dp.append([0, 1])

while t > 0:
    n = int(input())
    if len(dp) <= n:
        for i in range(len(dp), n + 1):
            dp_0 = dp[i - 1][0] + dp[i - 2][0]
            dp_1 = dp[i - 1][1] + dp[i - 2][1]
            dp.append([dp_0, dp_1])
    print(dp[n][0], dp[n][1])
    
    t -= 1