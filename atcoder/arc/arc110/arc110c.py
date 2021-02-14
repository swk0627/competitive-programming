n = int(input())
p = list(map(int, input().split()))
ans = []
bef = 1
for i in range(n - 1):
    if p[i] == bef:
        for j in range(i, bef - 1, -1):
            p[j], p[j - 1] = p[j - 1], p[j]
            ans.append(j)
        bef = i + 1
for j in range(n - 1, bef - 1, -1):
    p[j], p[j - 1] = p[j - 1], p[j]
    ans.append(j)

for i, p in enumerate(p, 1):
    if i != p:
        print(-1)
        exit()
print(*ans, sep='\n')