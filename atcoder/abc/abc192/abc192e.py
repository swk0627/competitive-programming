import heapq
n, m, x, y = map(int, input().split())
stks = [[] for _ in range(n)]
for _ in range(m):
    a, b, t, k = (map(int, input().split()))
    stks[a-1].append([b-1, t, k])
    stks[b-1].append([a-1, t, k])
INF = 100000000000001
dp = [ INF for i in range(n)]
dp[x-1] = 0
h = []
for li in stks[x-1]:
    h.append([li[1], li[0]])
heapq.heapify(h)
while h:
    t , v = heapq.heappop(h)
    if dp[v] != INF:
        continue
    dp[v] = t
    for i in stks[v]:
        if t % i[2]:
            s = (t//i[2]+1)*i[2]+i[1]
        else:
            s=t+i[1]
        heapq.heappush(h, (s, i[0]))
if dp[y-1] == INF: print(-1)
else: print(dp[y-1])