import sys
import heapq
n, m, x, y = map(int, sys.stdin.readline().split())
x -= 1
y -= 1
stks = [ [] for _ in range(n)]
for _ in range(m):
    a, b, t, k = map(int, sys.stdin.readline().split())
    stks[a-1].append((b-1, t, k))
    stks[b-1].append((a-1, t, k))
dp = [ -1 for _ in range(n)]
dp[x] = 0
h = []
for path in stks[x]:
    h.append((path[1], path[0]))
heapq.heapify(h)
while h:
    t, curr = heapq.heappop(h)
    if dp[curr] != -1:
        continue
    dp[curr] = t
    for path in stks[curr]:
        s = -(-t // path[2]) * path[2] + path[1]
        heapq.heappush(h, (s, path[0]))
else: print(dp[y])