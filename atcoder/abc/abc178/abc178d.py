s = int(input())
mod = int(1e9 + 7)
dp = [ 0 for _ in range(s+1)]
dp[0] = 1
for i in range(3, s+1):
    dp[i] = dp[i-1] + dp[i-3]
    dp[i] %= mod
print(dp[-1])