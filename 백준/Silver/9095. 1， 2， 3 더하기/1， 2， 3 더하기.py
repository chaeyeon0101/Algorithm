t = int(input())
dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4

def f(x):
    if dp[x] != 0:
        return dp[x]
        
    dp[x] = f(x - 1) + f(x - 2) + f(x - 3)
    return dp[x]

while t > 0:
    n = int(input())
    print(f(n))
    t -= 1