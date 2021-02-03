n, k = map(int, input().split())
h = list(map(int, input().split()))
dp = [float('inf')] * n
for i in range(n):
    if i == 0: dp[i] = 0
    elif i == 1: dp[i] = abs(h[i] - h[i-1])
    else:
        for step in range(1, i+1):
            if step > k: break
            min_cost = dp[i-step] + abs(h[i] - h[i-step])
            dp[i] = min(dp[i], min_cost)
print(dp[-1])