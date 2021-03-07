n, m = map(int, input().split())
a = list(map(int, input().split()))
poss = [ [] for _ in range(n)]
i = 0
for num in a:
    poss[num].append(i)
    i += 1
for i in range(n):
    pre = -1
    poss[i].append(n)
    for pos in poss[i]:
        if pos - pre > m:
            print(i)
            exit()
        pre = pos
print(m)