N, W = map(int, input().split())
w = [ 0 for _ in range(N+1)]
v = [ 0 for _ in range(N+1)]
for i in range(1, N+1): w[i], v[i] = map(int, input().split())
dp = [ [ float('inf') for _ in range(sum(v)+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, sum(v)+1):
        if j == v(i):
            dp[i][j] = min(dp[i-1][j], dp[i-1][j] + w[i])

for  in range(dp):

