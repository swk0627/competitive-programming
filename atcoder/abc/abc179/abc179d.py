n, k = map(int, input().split())
s = []
for _ in range(k):
    s.append(list(map(int, input().split())))
dp = [ 0 for _ in range(n)]
sdp = [ 0 for _ in range(n+1)]
dp[0] = 1
sdp[1] = 1
for i in range(1, n):
    for j in s:
        dp[i] += sdp[max(0, i - j[0] + 1)] - sdp[max(0, i - j[1])]
        dp[i] %= 998244353
    sdp[i+1] = sdp[i] + dp[i]
print(dp[-1])