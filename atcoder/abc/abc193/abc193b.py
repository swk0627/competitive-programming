n = int(input())
apxs = []
for _ in range(n):
    apxs.append(list(map(int, input().split())))
ans = 10000000000
for apx in apxs:
    tmp = apx[2] - apx[0]
    if tmp > 0: ans = min(ans, apx[1])
if ans == 10000000000: print(-1)
else: print(ans)