n, m = map(int, input().split())
a = list(map(int, input().split()))
routes = [ [] for _ in range(n)]
for _ in range(m):
    x, y = map(lambda x: int(x)-1, input().split())
    routes[x].append(y)
dp = [ 10000000000 for _ in range(n)]
for i in range(n):
    for j in routes[i]:
        dp[j] = min(dp[i], dp[j], a[i])
ans = -10000000000
for i in range(n):
    ans = max(ans, a[i] - dp[i])
print(ans)