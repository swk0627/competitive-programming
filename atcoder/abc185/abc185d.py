n, m = map(int, input().split())
intv = []

if m == n:
    print(0)
    exit()

elif m == 0:
    print(1)
    exit()

else:
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    a.insert(0, n+1)
    a.append(0)
    for i in range(len(a)-1):
        if a[i]-a[i+1]-1 != 0: intv.append(a[i]-a[i+1]-1)
    k = min(intv)
    ans = 0
    for i in intv:
        if i % k != 0: ans += i // k + 1
        else: ans += i // k
    print(ans)