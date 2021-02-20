n, a = tuple(input().split())
n = int(n)
ans = 0
for i in range(n):
    at_cnt = 0
    cg_cnt = 0
    for j in range(i, n):
        if a[j] == 'A':
            at_cnt += 1
        elif a[j] == 'T':
            at_cnt -= 1
        elif a[j] == 'C':
            cg_cnt += 1
        elif a[j] == 'G':
            cg_cnt -= 1
        if at_cnt == 0 and cg_cnt == 0: ans += 1
print(ans)