import itertools

n, k = map(int, input().split())
t = [ list(map(int, input().split())) for _ in range(n)]
cnt = 0
for i in itertools.permutations(range(1, n)):
    cost = 0
    former_j = 0
    for j in i:
        cost += t[former_j][j]
        former_j = j
    cost += t[former_j][0]
    if cost == k: cnt += 1
print(cnt)