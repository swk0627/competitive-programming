n = int(input())
dp = [[0] * 3 for _ in range(n + 1)]
A, B, C = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
for i in range(1, n+1):
    A[i], B[i], C[i] = map(int, input().split())
for i in range(1, n+1):
    print(dp)
    if i == 1:
        dp[i][0] = A[i]
        dp[i][1] = B[i]
        dp[i][2] = C[i]
    else:
        dp[i][0] = max(dp[i-1][1] + A[i], dp[i-1][2] + A[i])
        dp[i][1] = max(dp[i-1][0] + B[i], dp[i-1][2] + B[i])
        dp[i][2] = max(dp[i-1][0] + C[i], dp[i-1][1] + C[i])
print(max(dp[-1]))