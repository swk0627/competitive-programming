n, m, x, y = map(int, input().split())
abtks = []
for _ in range(m):
    abtks.append(list(map(int, input().split())))
INF = 100000000000001
dp = [ INF for i in range(n)]
dp[x-1] = 0
abtks.sort(reverse=True)
while abtks:
    abtk = abtks.pop()
    dp[abtk[1]-1] = min(dp[abtk[1]-1], abtk[2] + abtk[3] * -(-dp[abtk[0]-1] // abtk[3]))
    dp[abtk[0]-1] = min(dp[abtk[0]-1], abtk[2] + abtk[3] * -(-dp[abtk[1]-1] // abtk[3]))
if dp[y-1] == INF: print(-1)
else: print(dp[y-1])