a_size = int(input())
a = list(map(int, input().split()))
dp = [0] * a_size

for i in range(a_size):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
    
print(max(dp))