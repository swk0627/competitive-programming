n = int(input())
h = list(map(int, input().split()))
dp = [float('inf')] * n
for i in range(n):
    if i == 0:
        dp[i] = 0
    elif i == 1:
        dp[i] = abs(h[i-1] - h[i])
    else:
        dp[i] = min(dp[i-1]+abs(h[i]-h[i-1]), dp[i-2]+abs(h[i]-h[i-2]))
print(dp[-1])