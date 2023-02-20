import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0]

for _ in range(m):
    i, j = map(int, input().split())
    
    if j > len(dp) - 1:
        for k in range(len(dp), j + 1):
            dp.append(dp[k - 1] + arr[k - 1])
    
    print(dp[j] - dp[i - 1])